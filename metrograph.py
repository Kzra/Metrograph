# Task 4 Continued
# In order to show 4/4 time we can use a square and a triangle for 3/4
import turtle
import numpy as np
import time


def Metrograph():
    bpm = int(input('Bpm? '))
    size = 150
    time_sig = int(input('Time Sig? (give the upper-numerical) '))
    bpm = 60 / bpm
    i = 0 
    n = 1
    beat_counter = 1
    x_start_pos = 0
    y_start_pos = 0
    
    dur = True
	
    angle = 360 / time_sig
    
    if time_sig == 4:
        x_start_pos = size / 2
        y_start_pos = - x_start_pos
    elif  time_sig == 3 or time_sig == 6:
        x_start_pos = size / 2
        y_start_pos = - (np.sqrt(size**2 - x_start_pos **2) / 2) * (1 + ((time_sig-3)/4))
    else:
        x_start_pos = size / 2
        y_start_pos = -  (size/2) / (2*np.tan(((np.pi/2)/time_sig)))
   
    
    #initialise the graphics interface:
    turtle.color('black', 'blue')
    turtle.penup()
    turtle.begin_fill()
    turtle.shape('circle')
    turtle.speed(8)
    turtle.setpos(x_start_pos,y_start_pos)
    turtle.left(angle)
    turtle.forward(size)
    turtle.pendown()
    
    print('Press CTRL + C to exit') 
	
	
	#begin the metronome
    start = time.perf_counter()
    while dur == True:
        end = time.perf_counter()
        i = end - start
        if i - n > 0 and i - n < 0.00005:
            turtle.left(angle)
            turtle.forward(size)     
            n = n + bpm
            if beat_counter % time_sig == 1: 
                turtle.fillcolor('red')
            else:
                turtle.fillcolor('blue')
                
            beat_counter = beat_counter + 1

    print(beat_counter - 1)
    turtle.done()


Metrograph()