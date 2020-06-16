#!/usr/bin/env python3 

# requirements 
import selenium 
import os 
import datetime
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

def first():
    # getting ready 
    Notify.init("Test Notifier")
    notification = Notify.Notification.new("Hey!", "\nHow are you doing ?", "face-smile" ,) 
    


    notification.show()
    


def main(): 
    first()
    
    
if __name__=='__main__':main()
