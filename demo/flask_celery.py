from celery import Celery


def make_celery(app):
    celery_instance = Celery(app.import_name, backend=app.config['CELERY_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery_instance.conf.update(app.config)
    TaskBase = celery_instance.Task

    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery_instance.Task = ContextTask
    return celery_instance
