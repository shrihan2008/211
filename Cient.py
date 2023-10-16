import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path
global infolabel
global song_selected
from playsound import playsound
import pygame
from pygame import mixer

global song_counter
song_counter=0

for i in os.listdir("shared_files"):
    filename=os.decode(i)
    Listbox.insert(song_counter,filename)
    song_counter+=1

def play():
    global song_selected
    song_selected=Listbox.get(ANCHOR)
    mixer.music.load("shared_files/",song_selected)
    mixer.init()
    if(song_selected != ""):
        infolabel.configure(text="Now playing"+song_selected)
    else:
        print("not playing")

def stop():
    global song_selected
    mixer.init()
    mixer.music.load("shared_files/",song_selected)
    mixer.music.pause()
    infolabel.configure(text="")
    
def resume():
    global song_selected
    mixer.init()
    mixer.music.load("shared_files/",song_selected)
    mixer.music.resume()
   

def pause():
    global song_selected
    mixer.init()
    mixer.music.load("shared_files/",song_selected)
    mixer.music.pause()
   

resumeButton=Button(text="Resume",command=resume)
resumeButton.place(x=50,y=200)

pauseButton=Button(text="Pause",command=pause)
pauseButton.place(x=70,y=240)