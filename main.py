import time
from colorama import Fore
from pygame import mixer
from tkinter import *
import os
from pypresence import Presence



volume = 1.0

try:
    rpc = Presence(943584689241874452)
    rpc.connect()
    rpc.update(buttons=[{"label": "Download Here", "url": "https://noch-nicht.de"}], details="Listening Nothing",
               large_image="https://media.discordapp.net/attachments/920739361304244267/943585076845883412/Logo_Neu-tr.png?width=485&height=464",
               start=time.time())

except:
    pass


def playsong():
    currentsong = playlist.get(ACTIVE)
    print(Fore.GREEN + "Playing " + Fore.BLUE + currentsong.replace(".mp3", ""))

    rpc_song_update = currentsong.split(".", 1)
    try:
        rpc.update(buttons=[{"label": "Download Here", "url": "https://noch-nicht.de"}],
                   details=f'Listening {currentsong.replace(".mp3", "")}',
                   large_image="https://media.discordapp.net/attachments/920739361304244267/943585076845883412/Logo_Neu-tr.png?width=485&height=464",
                   start=time.time())

    except:
        pass

    song = mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()


def make_quieter():
    pass


def make_louder():
    mixer.music.set_volume()


def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

    try:
        rpc.update(buttons=[{"label": "Download Here", "url": "https://noch-nicht.de"}], details="Listening Nothing",
                   large_image="https://media.discordapp.net/attachments/920739361304244267/943585076845883412/Logo_Neu-tr.png?width=485&height=464",
                   start=time.time())
    except:
        pass


def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()
    try:
        rpc.update(buttons=[{"label": "Download Here", "url": "https://noch-nicht.de"}], details="Listening Nothing",
                   large_image="https://media.discordapp.net/attachments/920739361304244267/943585076845883412/Logo_Neu-tr.png?width=485&height=464",
                   start=time.time())
    except:
        pass

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

    currentsong = playlist.get(ACTIVE)

    try:
        rpc.update(buttons=[{"label": "Download Here", "url": "https://noch-nicht.de"}],
                   details=f'Listening {currentsong.replace(".mp3", "")}',
                   large_image="https://media.discordapp.net/attachments/920739361304244267/943585076845883412/Logo_Neu-tr.png?width=485&height=464",
                   start=time.time())
    except:
        pass

root = Tk()
root.title('Strawplayer')

mixer.init()
songstatus = StringVar()
songstatus.set("choosing")

# playlist---------------

playlist = Listbox(root, selectmode=SINGLE, bg="#F1F3F7", fg="Black", font=('arial', 15), width=40)
playlist.grid(columnspan=5)

with open("path.conf", "r") as config:
    path = config.read()

print(path)
os.chdir(r"" + path)
songs = os.listdir()
for s in songs:
    playlist.insert(END, s)

playbtn = Button(root, text="Play", command=playsong)
playbtn.config(font=('arial', 20), bg="#E5E7EA", fg="white", padx=7, pady=7)
playbtn.grid(row=1, column=0)

pausebtn = Button(root, text="Pause", command=pausesong)
pausebtn.config(font=('arial', 20), bg="#E5E7EA", fg="white", padx=7, pady=7)
pausebtn.grid(row=1, column=1)

Resumebtn = Button(root, text="Resume", command=resumesong)
Resumebtn.config(font=('arial', 20), bg="#E5E7EA", fg="white", padx=7, pady=7)
Resumebtn.grid(row=1, column=3)

stopbtn = Button(root, text="Stop", command=stopsong)
stopbtn.config(font=('arial', 20), bg="#E5E7EA", fg="white", padx=7, pady=7)
stopbtn.grid(row=1, column=2)

volume = Scale(root, from_=1, to=100)
volume.grid(row=1, column=4)

mainloop()