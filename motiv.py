#! /usr/bin/env python3 

# I hate importing, I need to import someshit in case if I need 'em 
import os, random  
from random import randint
from datetime import datetime 
from numpy.random import seed
from numpy.random import rand 
import time 
import notifier 

def today(): 
    # Some problem managing the right time (It won't matter much) 
    today = datetime.today() 
    t = time.localtime() 
    current = time.strftime("%H:%M:%S", t) 
    #print(current)
    stc = str(current) 
    # current hour
    ch = str(current[0]) + str(current[1]) 
    ch = ch - 1 
    # current minute 
    cm = str(current[3]) + str(current[4]) 
    # current seconde 
    cs = str(current[6]) + str(current[7])
    #print(ch,cm,cs)
    """
    rch = rand(int(ch)) 
    rcm = rand(int(cm)) 
    rcs = rand(int(cs)) 
    print(rch, rcm, rcs) 
    
    """
    """
    cv = randint(1,int(ch)) 
    #print(cv) 
    if 10 > cv:
        # Edit the path 
        os.system('python3 /home/mohamed/Desktop/mytools/Motiv/notifier.py') 
    elif cv > 18: 
        os.system('python3 /home/mohamed/Desktop/mytools/Motiv/notifier.py') 


    """

    #print(ch)
def main():
    
    today()

if __name__='__name__':main()
