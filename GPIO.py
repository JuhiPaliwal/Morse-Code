""" Author : Juhi Paliwal and Arunima Mookherjee
    Last Modified : Sat, Apr 16 2016 18:16:46
    MORSE CODE GENERATOR BUILT ON RASPBERRY PI
"""

import time
import RPi.GPIO as GPIO
GPIO.setsmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.cleanup()
on_time=3
on_short_time=1
off_time=1
word=input("Enter the word you wish to display MORSECODE of....")
print(word)
i=0
while i < len(word):
	if word[i] == 'a'
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return

    elif word[i] == 'b'
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return

    elif word[i] == 'c'
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return

    elif word[i] == 'd':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return
	
    elif word[i] == 'e':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return
	
    elif word[i] == 'f':
	GPIO.output(12,1)
	time.sleep(on_short_time)
	GPIO.output(12,0)
	time.sleep(off_time)
	GPIO.output(12,1)
	time.sleep(on_short_time)
	GPIO.output(12,0)
	time.sleep(off_time)
	GPIO.output(12,1)
	time.sleep(on_time)
	GPIO.output(12,1)
	time.sleep(off_time)
	GPIO.output(12,1)
	time.sleep(on_short_time)
	GPIO.output(12,0)
	return
	
    elif word[i] == 'g':
		GPIO.output(12,1)
        time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
        time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return
	
    elif word[i] == 'h':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return
	
    elif word[i] == 'i':
		GPIO.output(12,1);
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return
	
    elif word[i] == 'j':
		GPIO.output(12,1);
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return

    elif word[i] == 'k':
		GPIO.output(12,1)
        time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
 	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
        time.sleep(on_time)
	    GPIO.output(12,0)
	    return

    elif word[i] == 'l':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    return

    elif word[i] == 'm':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return

    elif word[i] == 'n':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return

    elif word[i] == 'o':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
     	GPIO.output(12,0)
	    return

    elif word[i] == 'p':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return
	    
	elif word[i] == 'q':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return
	
    elif word[i] == 'r':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return
	
    elif word[i] == 's':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return

    elif word[i] == 't':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return
	
    elif word[i] == 'u':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return	

    elif word[i] == 'v':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return	
	
    elif word[i] == 'w':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return	
	
    elif word[i] == 'x':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return	
	
    elif word[i] == 'y':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return	
	
    elif word[i] == 'z':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return	
	
    elif word[i] == '1':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return
    
    elif word[i] == '2':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return   
	
    elif word[i] == '3':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return 
	
    elif word[i] == '4':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return  
	
    elif word[i] == '5':
		GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
 	    GPIO.output(12,0)
	    return  

    elif word[i] == '6':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return  

    elif word[i] == '7':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return 	
	    
	elif word[i] == '8':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return 	
	
    elif word[i] == '9':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
 	    GPIO.output(12,1)
	    time.sleep(on_short_time)
	    GPIO.output(12,0)
	    return   
	
    elif word[i] == '0':
		GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    time.sleep(off_time)
	    GPIO.output(12,1)
	    time.sleep(on_time)
	    GPIO.output(12,0)
	    return   
	    
	    i=i+1
	
GPIO.output(12,1)
time.sleep(5)
GPIO.output(12,0)
