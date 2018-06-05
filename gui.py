
#just tryin make uh good good ui

#Known errors:
#Twitter function runs on startup

#first test
import tkinter as tk
from tkinter import *
#from tkinter.ttk import *
from tkinter import messagebox
from reddit import reddit_osint
import subprocess as sub
import tkinter.scrolledtext as tkst
import traceback
import sys
from twitter import twitter


window = Tk()

window.title("This will be the OSINT dashboard")

#eventually the functions will run the osint
def clicked_face():
    facebook=Toplevel(bg='#3b5998')
    facebook.title("FACEBOOK OSINT")
    facelbl=Label(facebook, text="osinting the facebook", bg='#3b5998', font=(20), height=10, width=25)
    facelbl.grid(row=0, column=0, columnspan=3)

def clear_text():
    window.text_box.configure(state="normal")
    window.text_box.delete(1.0, END)
    window.text_box.configure(state="disabled")

#change the label when hovering over a button for more info
def redd_label(event):
    lbl.configure(text="Search reddit")
def twit_label(event):
    lbl.configure(text="Search twitter")
def face_label(event):
    lbl.configure(text="Search facebook")
def revert_label(event):
    lbl.configure(text="Select the platform to search")


###################################
# Trying to output to GUI instead #
# of the console                  #
###################################
#functions to redirect console output to GUI
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

#display the output

window.text_box = tkst.ScrolledText(window, wrap='word', font=(20))
window.text_box.grid(row=4, column=0, columnspan=3, rowspan=1)
#sys.stdout = StdoutRedirector(window.text_box)
#sys.stderr = StdoutRedirector(window.text_box)
sys.last_traceback = StdoutRedirector(window.text_box)


#formatting gui window
lbl=Label(window, text="Select the platform to search")
lbl.grid(row=0, column=0, columnspan=3)
padlbl=Label(window, height=1)
padlbl.grid(row=3)
padlbl=Label(window, height=1)
padlbl.grid(row=5)

#btn stuff
#first reddit
reddit_btn = Button(window, text="Reddit OSINT", bg='#FF4500', height=5, width=25, command=reddit_osint)
reddit_btn.grid(row=2, column=0)
reddit_btn.bind("<Enter>", redd_label)
reddit_btn.bind("<Leave>", revert_label)
#then twitter
twitter_btn = Button(window, text="Twitter OSINT", bg='#0084b4', height=5, width=25, command=twitter) #modifying this line
twitter_btn.grid(row=2, column=1)
twitter_btn.bind("<Enter>", twit_label)
twitter_btn.bind("<Leave>", revert_label)
#and facebook too
facebook_btn = Button(window, text="Facebook OSINT", bg='#3b5998', height=5, width=25, command=clicked_face)
facebook_btn.grid(row=2, column=2)
facebook_btn.bind("<Enter>", face_label)
facebook_btn.bind("<Leave>", revert_label)
#clear text button
clear_text=Button(window, text="Clear", command=clear_text)
clear_text.grid(row=6, column=2)


window.mainloop()
