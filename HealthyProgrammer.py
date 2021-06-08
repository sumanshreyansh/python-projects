#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log

# Rules
# Pygame module to play audio
# You will have to manage the clashes between the reminders 
# such that no two reminders play at the same time.

import time
import datetime
import pygame
from pygame import mixer

print("welcome to health tracker")
current_time = time.strftime("%H:%M:%S")
strt_time = "09:00:00"
end_time = "17:00:00"

# water configuration
wt_limit = 3500
glass = 200
no_of_glass = round(wt_limit / glass)
working_time = 8*60*60
water_interval = working_time / no_of_glass 
water_song = "water.mp3"

# eye exercise configuration 
eye_interval = 30*60
eye_song = "eye.mp3"

# physical exercise configuration
physical_interval = 45*60
physical_song = "physical.mp3"

def music(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

def water_drinking_reminder(water):
    i = input("if you drank the water,please write drank: ").lower()
    while(i != "drank"):
        music(water_song)
        print("\n",end="")
        if i == "drank":
            data = input("if done type here\n")
            f = open("water-record.txt","a")
            f.write(str([str(gettime())])+": "+data+"\n")   
            f.close()
            print("Thank you")
            mixer.music.stop()
            time.sleep(water_interval)
            break

def physical_exercise_reminder(exercise):
    i = input("if you finish the exercise,please write finished: ").lower()
    while(i != "finished"):
        music(physical_song)
        print("\n",end="")
        if i == "finished":
            data = input("if done type here\n")
            f = open("phyexe-record.txt","a")
            f.write(str([str(gettime())])+": "+data+"\n")   
            f.close()
            print("Thank you")
            mixer.music.stop()
            time.sleep(physical_interval)
            break

def eye_exercise_reminder(eye):
    i = input("if you finish the eye exercise,please write done: ").lower()
    while(i != "done"):
        music(eye_song)
        print("\n",end="")
        if i == "done":
            data = input("if done type here\n")
            f = open("eyeexe-record.txt","a")
            f.write(str([str(gettime())])+": "+data+"\n")   
            f.close()
            print("Thank you")
            mixer.music.stop()
            time.sleep(eye_interval)
            break

