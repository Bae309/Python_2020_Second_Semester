from tkinter import *

window = Tk()
window.title("고양이들~~~")

photo1=PhotoImage(file="../gif/cat.gif")
label1=Label(window, image=photo1)

photo2=PhotoImage(file="../gif/cat2.gif")
label2=Label(window, image=photo2)

photo3=PhotoImage(file="../gif/cat3.gif")
label3=Label(window, image=photo3)

label1.pack(side=TOP)
label2.pack(side=TOP)
label3.pack(side=TOP)

window.mainloop()
