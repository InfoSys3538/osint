#just tryin make uh good good ui

#first test
from Tkinter import *

window = Tk()
#ya boi, get that window size
window.geometry('1000x750')

window.title("This will be the OSINT dashboard")

btn = Button(window, text="Reddit OSINT")

btn.grid(column=1, row=0)

window.mainloop()
