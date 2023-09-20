from tkinter import *

window = Tk()

btnList=[""]*5

for i in range(0,5):
    btnList[i]=Button(window, text="버튼"+str(i+1))

'''button1=Button(window, text="버튼1")
button2=Button(window, text="버튼2")
button3=Button(window, text="버튼3")
button1.pack(side=TOP)
button2.pack(side=TOP)
button3.pack(side=TOP)'''

for btn in btnList:
    btn.pack(side=TOP, fill=X, padx=10, pady=10, ipadx=10, ipady=10)

window.mainloop()
