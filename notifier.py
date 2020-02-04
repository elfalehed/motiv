#! /usr/bin/env python3

# requirements 

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Test Notifier")

#def main(): 
 #  notification = Notify.Notification.new(
  #         "Hey!", "\nHow are you doing ?",
   #     "face-smile" ,  
           #  )
#   notification.show() 


#def status(): 
     


def notify(self, msg, title="Ava Message"):
    if self.notification is None:
        self.notification = Notify.Notification.new(
            title,
            msg,
            resource_path("res/icon.png"))
        self.notification.set_app_name("EAvatar")
    else:
        self.notification.update(title, msg)
    self.notification.set_timeout(3)
    self.notification.show()



