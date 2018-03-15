from demo import app
from .notifcations import NotificationService


@app.route('/some-controller/')
def some_controller():
    """
    This controller in your flask web app that processes a
    request and returns a response
    """
    notify = NotificationService()
    notify.send_notification('CALM SYSTEM')
    return "Made an async call to notify"
