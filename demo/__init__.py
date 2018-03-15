from flask import Flask
from .flask_celery import make_celery

app = Flask(__name__)

"""
redis dependency is injected at app creation time. redis can be substituted for RabbitMQ
with out break any other modules in the application.
"""
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379'
app.config['CELERY_BACKEND'] = 'redis://localhost:6379'

celery = make_celery(app)

from demo import views