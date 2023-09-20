from tkinter import *
from tkinter import messagebox

##
def myFunc():
    messagebox.showinfo("강아지버튼","강아지가 귀엽죠?^^")

##
window=Tk()

photo=PhotoImage(file="../gif/dog2.gif")
button = Button(window, image = photo, command = myFunc)

button.pack()

window.mainloop()

