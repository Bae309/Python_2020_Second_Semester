from tkinter import *

window = Tk()

button1 = Button(window, text = "hello", fg = "yellow", bg = "red", command = quit)

button1.pack()

window.mainloop()
