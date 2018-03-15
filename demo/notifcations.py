import abc
from demo import celery


class abstractNotification(metaclass=abc.ABCMeta):
    """
    Define an interface to be used by clients to send notifications
    """

    @staticmethod
    @abc.abstractmethod
    def send_notification():
        pass


@celery.task(name='demo.notify')
def send_celery_notification():
    """
    A long procedure can be;
    1. A database read/write operation
    2. Connecting to an external service to receive/send data e.g Twitter, SMS gateway
    3. Connecting to an Email server to send bulk email
    """
    print("this some long procedure that runs async, bye!")


class NotificationService(abstractNotification):
    """
    concrete class that implements abcNotification interface
    """

    @staticmethod
    def send_notification(payload=""):
        send_celery_notification.delay()
        print('payload: {}'.format(payload))
        print('sending a notification...')
