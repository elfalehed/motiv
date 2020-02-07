#!/usr/bin/env python3 

# requirements 
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Test Notifier")
# new comment 
def main(): 
  notification = Notify.Notification.new(
      "Hey!", "\nHow are you doing ?",
   "face-smile" ,  
  )
   notification.show() 


if __name__ == '__main__':main()

