from tkinter import *

window=Tk()

window.title("내 꺼")
##window.geometry("400x100")
window.resizable(width=FALSE, height=FALSE)

level1=Label(window, text = "안녕하세요...배성윤입니다.")
level2=Label(window, text = "열심히", font = ("궁서체",30), bg="yellow", fg="red")
level3=Label(window, text = "공부 중입니다.", bg="magenta", fg="blue", width=20, height=5, anchor=SE)

level1.pack();
level2.pack();
level3.pack();
window.mainloop()

window2=Tk()

photo=PhotoImage(file="../gif/dog.gif") ## 상대경로 표기법
label4=Label(window2, image=photo)

label4.pack();
window2.mainloop()
