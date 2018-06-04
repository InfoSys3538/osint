#just tryin make uh good good ui

#first test
import tkinter as tk
from tkinter import *
#from tkinter.ttk import *
from tkinter import messagebox
from reddit_test import reddit_osint
import subprocess as sub
import traceback
import sys


window = Tk()

window.title("This will be the OSINT dashboard")

###################################
# Trying to output to GUI instead #
# of the console                  #
###################################

#eventually the functions will run the osint
def clicked_redd():
    reddit=Toplevel(bg='#FF4500')
    reddit.title("REDDIT OSINT")
    redlbl=Label(reddit, text="osinting the reddit", bg='#FF4500', font=(20))
    redlbl.grid(row=0, column=0, columnspan=3)
    reddbtn=Button(reddit, text="Press to osint reddit", bg='#FF4500', height=10, width=25, command=reddit_osint)
    reddbtn.grid(row=1, column=0)

def clicked_twit():
    twitter=Toplevel(bg='#0084b4')
    twitter.title("TWITTER OSINT")
    twitlbl=Label(twitter, text="osinting the twitter", bg='#0084b4', font=(20), height=10, width=25)
    twitlbl.grid(row=0, column=0, columnspan=3)

def clicked_face():
    facebook=Toplevel(bg='#3b5998')
    facebook.title("FACEBOOK OSINT")
    facelbl=Label(facebook, text="osinting the facebook", bg='#3b5998', font=(20), height=10, width=25)
    facelbl.grid(row=0, column=0, columnspan=3)

def clear_text():
    window.text_box.configure(state="normal")
    window.text_box.delete(1.0, END)
    window.text_box.configure(state="disabled")


class IORedirector(object):
   '''A general class for redirecting I/O to this Text widget.'''
   def __init__(window,text_area):
      window.text_area = text_area

class StdoutRedirector(IORedirector):
   '''A class for redirecting stdout to this Text widget.'''
   def write(window,message):
      window.text_area.insert("insert", message)
      window.text_area.config(state = "normal")
      window.text_area.config(state = "disabled")

window.text_box = Text(window, wrap='word')

lbl=Label(window, text="Select the platform to search")
lbl.grid(row=0, column=0, columnspan=3)
padlbl=Label(window, height=1)
padlbl.grid(row=3)
window.text_box.grid(row=4, column=0, columnspan=3, rowspan=1)
padlbl=Label(window, height=1)
padlbl.grid(row=5)
sys.stdout = StdoutRedirector(window.text_box)
sys.stderr = StdoutRedirector(window.text_box)
detail = traceback.format_exc()
detail = StdoutRedirector(window.text_box)


#btn stuff
#first reddit
reddit_btn = Button(window, text="Reddit OSINT", bg='#FF4500', height=5, width=25, command=reddit_osint)
reddit_btn.grid(row=2, column=0)
#then twitter
twitter_btn = Button(window, text="Twitter OSINT", bg='#0084b4', height=5, width=25, command=clicked_twit)
twitter_btn.grid(row=2, column=1)
#and facebook too
facebook_btn = Button(window, text="Facebook OSINT", bg='#3b5998', height=5, width=25, command=clicked_face)
facebook_btn.grid(row=2, column=2)
#clear text button
clear_text=Button(window, text="Clear", command=clear_text)
clear_text.grid(row=6, column=2)


window.mainloop()
