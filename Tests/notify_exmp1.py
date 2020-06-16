#! /usr/bin/env python3 
# requirments
import gi 
gi.require_version('Notify', '0.7') 
from gi.repository import Notify 


def send_notification(title, text):
    try:
        if Notify.init(argv[0]):
            n = Notify.Notification.new("Notify")
            n.update(title, text)
            n.set_urgency(2)
            if not n.show():
                raise SyntaxError("sending notification failed!")
        else:
            raise SyntaxError("can't initialize notification!")
    except SyntaxError as error:
        print(error)
        if error == "sending notification failed!":
            Notify.uninit()
    else:
        Notify.uninit() 

send_notification("Test","hello")









