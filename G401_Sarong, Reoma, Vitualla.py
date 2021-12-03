#File:				G401_Group 5_Code
#Author:			Sarong, et. al
#Date created:		12/2/2021
#Checkpoint:        Checkpoint 03

import time

print("Pomodoro begins now.")
t = 1*60
while t:
   mins = t // 60
   secs = t%60
   timer = '{:02d} : {:02d}'.format(mins, secs)
   print(timer, end="\r")
   time.sleep(1)
   t -= 1
   
print('It is breaktime!')
t = 1*60
while t:
   mins = t // 60
   secs = t%60
   timer = '{:02d} : {:02d}'.format(mins, secs)
   print(timer, end="\r")
   time.sleep(1)
   t -= 1

print("It is now time for pomodoro.")
t = 1*60
while t:
   mins = t // 60
   secs = t%60
   timer = '{:02d} : {:02d}'.format(mins, secs)
   print(timer, end="\r")
   time.sleep(1)
   t -= 1
   
print('It is breaktime!')
t = 1*60
while t:
   mins = t // 60
   secs = t%60
   timer = '{:02d} : {:02d}'.format(mins, secs)
   print(timer, end="\r")
   time.sleep(1)
   t -= 1
   
print("It is now time for pomodoro.")
t = 1*60
while t:
   mins = t // 60
   secs = t%60
   timer = '{:02d} : {:02d}'.format(mins, secs)
   print(timer, end="\r")
   time.sleep(1)
   t -= 1
   
print('It is breaktime!')
t = 1*60
while t:
   mins = t // 60
   secs = t%60
   timer = '{:02d} : {:02d}'.format(mins, secs)
   print(timer, end="\r")
   time.sleep(1)
   t -= 1
  
print("It is now time for pomodoro.")
t = 1*60
while t:
   mins = t // 60
   secs = t%60
   timer = '{:02d} : {:02d}'.format(mins, secs)
   print(timer, end="\r")
   time.sleep(1)
   t -= 1
   
print('It is breaktime!')
t = 1*60
while t:
   mins = t // 60
   secs = t%60
   timer = '{:02d} : {:02d}'.format(mins, secs)
   print(timer, end="\r")
   time.sleep(1)
   t -= 1  
 
print("Four pomodoro is done. Duration of breaktime can be 15-20 minutes.")
print()
print("It is now time for pomodoro.")
t = 1*60
while t:
   mins = t // 60
   secs = t%60
   timer = '{:02d} : {:02d}'.format(mins, secs)
   print(timer, end="\r")
   time.sleep(1)
   t -= 1
   
print('It is breaktime!')
t = int(input("Enter duration of breaktime in seconds: "))
while t:
   mins = t // 60
   secs = t%60
   timer = '{:02d} : {:02d}'.format(mins, secs)
   print(timer, end="\r")
   time.sleep(1)
   t -= 1