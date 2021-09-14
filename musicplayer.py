import os
from tkinter.filedialog import askdirectory

import pygame
from mutagen.id3 import ID3
from tkinter import *

from mutagen.mp3 import MP3
import threading
import time
import datetime

root = Tk()
root.minsize(600,600)
root.title('Music Pylayer')

listofsongs = []
realnames = []

lengthofsongs=[]

v = StringVar()

q=StringVar()
s=StringVar()

volLabel=StringVar()

songlabel = Label(root,textvariable=v,width=35)
songlabel2 = Label(root,textvariable=q,width=35)
songlabel3 = Label(root,textvariable=s,width=35)

volume=Label(root,textvariable=volLabel,width=35)

index = 0

counter=0
def clocker(event):
    while(event==None):
        clock = pygame.time.Clock()
        print(clock)
        
def update_label(self):
    self.label.configure(cpuTemp)
    self.root.after(1000, self.update_label)
def updatelabel():
    global index
    global songname
    v.set('Current Song: '+realnames[index])
    q.set('Status: Playing')
    print(pygame.mixer.music.get_pos(),'lol')
    clock = pygame.time.Clock()
    print(clock)
    volLabel.set("Current Volume: "+str(pygame.mixer.music.get_volume()))
    s.set('Timer:  '+str(datetime.timedelta(seconds=pygame.mixer.music.get_pos()//1000)))
    t = threading.Timer(1.0, updateTimer)
    t.start()
    if(pygame.mixer.music.get_busy()==False):
        q.set('Status: Not Playing')
        
    #return songname

def updateTimer():
    while(pygame.mixer.music.get_busy()==True):
##        s.set('Timer:  '+str(pygame.mixer.music.get_pos()//1000))
        s.set('Timer:  '+str(datetime.timedelta(seconds=pygame.mixer.music.get_pos()//1000)))
        time.sleep(1)
        #break
    
        
def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        print(os.listdir(directory),'s')
        print(files,'files')
        filename=str(files)
        print(filename)
        if files.endswith(".mp3"):
            global counter
            counter=counter+1
            print('1')
            realdir = os.path.realpath(files)
            print('2')
            audio = ID3(realdir)
            print('3', audio)
            #realnames.append(audio['TSSE'].text[0])
            realnames.append(filename)
            print('4')
            

            listofsongs.append(files)
            print(listofsongs,'los')
            song = MP3(files)
            songLength = song.info.length
            lengthofsongs.append(songLength)

    pygame.mixer.init(44100)
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
    updatelabel()
    #clocker()
    
    print('lenght',lengthofsongs)
        

directorychooser()


def nextsong(event):
    print('eevent',event)
    global index
    global counter
    index = (index+1)%counter
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    global counter
    index = (index-1)%counter
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("No song playing")
    s.set('Timer: 00:00:00 ')
    #return songname

def pausesong(event):
    pygame.mixer.music.pause()
    
def playsong(event):
    pygame.mixer.music.unpause()
    updatelabel()

    #clocker()

def increaseVol(event):
    current=pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(current+0.1)
    volLabel.set("Current Volume: "+str(pygame.mixer.music.get_volume()))

    
def decreaseVol(event):
    current=pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(current-0.1)
    volLabel.set("Current Volume: "+str(pygame.mixer.music.get_volume()))

label = Label(root,text='Welcome!')
label.pack()

listbox = Listbox(root)
listbox.pack()

#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()
#listofsongs.reverse()


nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()

previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()

stopbutton = Button(root,text='Stop Music')
stopbutton.pack()

pausebutton = Button(root,text='Pause Music')
pausebutton.pack()

playbutton = Button(root,text='Play Music')
playbutton.pack()

increasevolbutton = Button(root,text='+ Volume')
increasevolbutton.pack()

decreasevolbutton = Button(root,text='- Volume')
decreasevolbutton.pack()


nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
pausebutton.bind("<Button-1>",pausesong)
playbutton.bind("<Button-1>",playsong)
#current=pygame.mixer.music.get_volume()
increasevolbutton.bind("<Button-1>",increaseVol)
decreasevolbutton.bind("<Button-1>",decreaseVol)

songlabel.pack()
songlabel2.pack()
songlabel3.pack()

volume.pack()


pygame.mixer.music.set_volume(0.5)
root.mainloop()
