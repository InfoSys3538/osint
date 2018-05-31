#just tryin make uh good good ui

#first test
from Tkinter import *

window = Tk()

#ya boi, get that window size
window.geometry('1000x750')

window.title("This will be the OSINT dashboard")

#btn stuff
#first reddit
reddit_btn = Button(window, text="Reddit OSINT", bg='#FF4500')
reddit_btn.grid(row=0, column=0)
#then twitter
twitter_btn = Button(window, text="Twitter OSINT", bg='#0084b4')
twitter_btn(row=1, column=0)


window.mainloop()
