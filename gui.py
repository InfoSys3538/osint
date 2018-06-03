#just tryin make uh good good ui

#first test
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()

#ya boi, get that window size
#window.geometry('700x500')

window.title("This will be the OSINT dashboard")

#eventually the functions will run the osint
def clicked_redd():
    #messagebox.showinfo('REDDIT OSINT', 'osinting the reddit')
    reddit=Toplevel(bg='#FF4500')
    #reddit.geometry('500x350')
    reddit.title("REDDIT OSINT")
    redlbl=Label(reddit, text="osinting the reddit", bg='#FF4500', font=(20), height=10, width=25)
    redlbl.grid(row=0, column=0, columnspan=3)

def clicked_twit():
    #messagebox.showinfo('TWITTER OSINT', 'osinting the twitter')
    twitter=Toplevel(bg='#0084b4')
    #twitter.geometry('500x350')
    twitter.title("TWITTER OSINT")
    twitlbl=Label(twitter, text="osinting the twitter", bg='#0084b4', font=(20), height=10, width=25)
    twitlbl.grid(row=0, column=0, columnspan=3)

def clicked_face():
    #messagebox.showinfo('FACEBOOK OSINT', 'osinting the facebook')
    facebook=Toplevel(bg='#3b5998')
    #facebook.geometry('500x350')
    facebook.title("FACEBOOK OSINT")
    facelbl=Label(facebook, text="osinting the facebook", bg='#3b5998', font=(20), height=10, width=25)
    facelbl.grid(row=0, column=0, columnspan=3)



lbl=Label(window, text="Select the platform to search")
lbl.grid(row=0, column=0, columnspan=3)

#btn stuff
#first reddit
reddit_btn = Button(window, text="Reddit OSINT", bg='#FF4500', height=5, width=25, command=clicked_redd)
reddit_btn.grid(row=2, column=0)
#then twitter
twitter_btn = Button(window, text="Twitter OSINT", bg='#0084b4', height=5, width=25, command=clicked_twit)
twitter_btn.grid(row=2, column=1)
#and facebook too
facebook_btn = Button(window, text="Facebook OSINT", bg='#3b5998', height=5, width=25, command=clicked_face)
facebook_btn.grid(row=2, column=2)

window.mainloop()
