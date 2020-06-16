#! /usr/bin/env python3 

import os 
import gi 
gi.require_version('Notify', '0.7') 
from gi.repository import Notify 
def backup(_):
    backuplaptop_callback_func()
    
    Notify.init("App Name")
    # Create the notification object
    summary = "Backing up!"
    body = "Meeting at 3PM!"
    icon = "/usr/share/icons/gnome/24x24/emotes/face-smile-big.png"
    notification = Notify.Notification.new(
        summary,
        body, # Optional
        icon, 
    )
    notification.add_action(
        "action_click",
        "Reply to Message",
        backuplaptop_callback_func,
        None # Arguments
    )
    notification.show
backup()

