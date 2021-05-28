#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
from pygame import mixer
import datetime
import time
import os
 
 
 
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            mixer.init()
            mixer.music.load(r"C:\Users\divya\PycharmProjects\alarm_clock\Ay Pilla.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            
            
                                   
          #  winsound.PlaySound(r"C:\Users\divya\PycharmProjects\alarm_clock\Ay Pilla.mp3",winsound.SND_ASYNC)
            break
 
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
 
clock = Tk()
clock.title("My Alarm Clock")
clock.geometry("500x500")

#background=r"C:\Users\divya\Desktop\alarm-clock.jpg"
#l=Label(clock,image=background)
#l.image=background
#l.grid()

time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",font="Roboto").place(x=120,y=350)
addTime = Label(clock,text = "Hour  Min   Sec",font=("Caveat",25,"italic")).place(x = 130,y=50)
#setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)
 
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
 
#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",font=10,width = 5).place(x=120,y=140)
minTime= Entry(clock,textvariable = min,bg = "pink",font=10,width = 5).place(x=210,y=140)
secTime = Entry(clock,textvariable = sec,bg = "pink",font=10,width =5).place(x=300,y=140)
 
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",font=("Roboto",20),width =20,command = actual_time).place(x =110,y=250)
 

clock.mainloop()
#Execution of the window.
