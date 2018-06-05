
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
from tkinter.font import Font
import csv


window = Tk()

window.title("This will be the OSINT dashboard")

text_input1=Entry(window, font=('Times', 20))
text_input2=Entry(window, font=('Times', 20))
text_input3=Entry(window, font=('Times', 20))
text_input4=Entry(window, font=('Times', 20))
text_input5=Entry(window, font=('Times', 20))
text_input6=Entry(window, font=('Times', 20))
text_input7=Entry(window, font=('Times', 20))
text_input8=Entry(window, font=('Times', 20))


#eventually the functions will run the osint
def clicked_face():
    facebook=Toplevel(bg='#3b5998')
    facebook.title("FACEBOOK OSINT")
    facelbl=Label(facebook, text="osinting the facebook", bg='#3b5998', font=('Times', 20), height=10, width=25)
    facelbl.grid(row=0, column=0, columnspan=3)

def clear_text():
    window.text_box.configure(state="normal")
    window.text_box.delete(1.0, END)
    window.text_box.configure(state="disabled")

#change the label when hovering over a button for more info
def redd_label(event):
    lbl.configure(text="Search reddit", font=('Times', 12))
def twit_label(event):
    lbl.configure(text="Search twitter", font=('Times', 12))
def face_label(event):
    lbl.configure(text="Search facebook", font=('Times', 12))
def revert_label(event):
    lbl.configure(text="Select the platform to search", font=('Times', 12))

#create entry widgets for user input
def user_input():
    def clear_twit():
        label_input1.grid_forget()
        label_input2.grid_forget()
        label_input3.grid_forget()
        label_input4.grid_forget()
        label_input5.grid_forget()
        label_input6.grid_forget()
        label_input7.grid_forget()
        text_input1.grid_forget()
        text_input2.grid_forget()
        text_input3.grid_forget()
        text_input4.grid_forget()
        text_input5.grid_forget()
        text_input6.grid_forget()
        text_input7.grid_forget()
        submit_btn.grid_forget()
        clear_twit_btn.grid_forget()

    label_input1=Label(window, text="Enter consumer key", font=('Times', 12))
    label_input1.grid()
    text_input1.grid()
    label_input2=Label(window, text="Enter consumer secret:", font=('Times', 12))
    label_input2.grid()
    text_input2.grid()
    label_input3=Label(window, text="Enter access token:", font=('Times', 12))
    label_input3.grid()
    text_input3.grid()
    label_input4=Label(window, text="Enter access token secret: ", font=('Times', 12))
    label_input4.grid()
    text_input4.grid()
    label_input5=Label(window, text="Enter latitude:", font=('Times', 12))
    label_input5.grid()
    text_input5.grid()
    label_input6=Label(window, text="Enter longitude:", font=('Times', 12))
    label_input6.grid()
    text_input6.grid()
    label_input7=Label(window, text="Enter radius:", font=('Times', 12))
    label_input7.grid()
    text_input7.grid()
    submit_btn=Button(window, text="Submit", font=('Times', 12), command=submit_twit)
    submit_btn.grid()
    clear_twit_btn = Button(window, text="Clear", font=('Times', 12), command=clear_twit)
    clear_twit_btn.grid()

def submit_twit():
    cK=text_input1.get()
    cS=text_input2.get()
    aT=text_input3.get()
    aS=text_input4.get()
    lat=text_input5.get()
    long=text_input6.get()
    rad=text_input7.get()
    twitter(cK, cS, aT, aS, lat, long, rad)
   #with open("twitterdata.csv", newline = "") as file:
       #reader = csv.reader(file)

       # r and c tell us where to grid the labels
      #r = 0
       #for col in reader:
          #c = 0
          #for row in col:
             # i've added some styling
             #label = Label(window, width = 10, height = 2, \
                                   #text = row, relief = RIDGE)
             #label.grid(row = r, column = c)
             #c += 1
          #r += 1

def redd_input():
    def clear_redd():
        redd_lbl.grid_forget()
        text_input8.grid_forget()
        redd_sub_btn.grid_forget()
        clear_redd_btn.grid_forget()
        #label.grid_forget()
    redd_lbl=Label(window, text="Enter the subreddit to scrape:", font=('Times', 12))
    redd_lbl.grid()
    text_input8.grid()
    redd_sub_btn=Button(window, text="Submit", font=('Times', 12), command=submit_redd)
    redd_sub_btn.grid()
    clear_redd_btn = Button(window, text="Clear", font=('Times', 12), command=clear_redd)
    clear_redd_btn.grid()

def submit_redd():
    subr=text_input8.get()
    reddit_osint(subr)



###################################
# Trying to output to GUI instead #
# of the console                  #
###################################
#functions to redirect console output to GUI
#class IORedirector(object):
#   '''A general class for redirecting I/O to this Text widget.'''
#   def __init__(window,text_area):
#      window.text_area = text_area

#class StdoutRedirector(IORedirector):
#   '''A class for redirecting stdout to this Text widget.'''
#   def write(window,message):
#      window.text_area.insert("insert", message)
#      window.text_area.config(state = "normal")
#      window.text_area.config(state = "disabled")
#   def flush(window):
#      pass


#display the output
#window.text_box = tkst.ScrolledText(window, wrap='word', font=(20))
#window.text_box.grid(row=4, column=0, columnspan=3, rowspan=1)
#sys.stdout = StdoutRedirector(window.text_box)
#sys.stderr = StdoutRedirector(window.text_box)
#sys.last_traceback = StdoutRedirector(window.text_box)


#formatting gui window
lbl=Label(window, text="Select the platform to search", font=('Times', 12))
lbl.grid(row=0, column=0, columnspan=3)
padlbl=Label(window, height=1)
padlbl.grid(row=3)
padlbl=Label(window, height=1)
padlbl.grid(row=5)

#btn stuff
#first reddit
reddit_btn = Button(window, text="Reddit OSINT", bg='#FF4500', font=('Times', 12), height=5, width=25, command=redd_input)
reddit_btn.grid(row=2, column=0)
reddit_btn.bind("<Enter>", redd_label)
reddit_btn.bind("<Leave>", revert_label)
#then twitter
twitter_btn = Button(window, text="Twitter OSINT", bg='#0084b4', font=('Times', 12), height=5, width=25, command=user_input)
twitter_btn.grid(row=2, column=1)
twitter_btn.bind("<Enter>", twit_label)
twitter_btn.bind("<Leave>", revert_label)
#and facebook too
facebook_btn = Button(window, text="Facebook OSINT", bg='#3b5998', font=('Times', 12), height=5, width=25, command=clicked_face)
facebook_btn.grid(row=2, column=2)
facebook_btn.bind("<Enter>", face_label)
facebook_btn.bind("<Leave>", revert_label)
#clear text button
#clear_text=Button(window, text="Clear", command=clear_text)
#clear_text.grid(row=6, column=2)


window.mainloop()
