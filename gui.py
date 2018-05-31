#just tryin make uh good good ui

#first test
from Tkinter import *
import tkFont

window = Tk()

#ya boi, get that window size
#window.geometry('1000x750')

window.title("This will be the OSINT dashboard")

#fonts
faceFont=tkFont.Font(family='Segoe UI')
twitterFont=tkFont.Font(family='Helvetica Neue')
redditFont=tkFont.Font(family='TS Volkswagen')

lbl=Label(window, text="Select the platform to search")
lbl.grid(row=0, column=0)

#btn stuff
#first reddit
reddit_btn = Button(window, text="Reddit OSINT", bg='#FF4500', height=5, width=25, font=redditFont)
reddit_btn.grid(row=1, column=0)
#then twitter
twitter_btn = Button(window, text="Twitter OSINT", bg='#0084b4', height=5, width=25, font=twitterFont)
twitter_btn.grid(row=2, column=0)
#and facebook too
facebook_btn = Button(window, text="Facebook OSINT", bg='#3b5998', height=5, width=25, font=faceFont)
facebook_btn.grid(row=3, column=0)



window.mainloop()
