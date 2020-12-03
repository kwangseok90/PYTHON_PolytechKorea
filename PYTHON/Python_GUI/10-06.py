from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 귀업습니다.")

window = Tk()

photo = PhotoImage("../../Test_Figure/GIF/cat.gif")
button1 = Button(window,image=photo,command=myFunc)

button1.pack()

window.mainloop()