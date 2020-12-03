from tkinter import *
from tkinter import messagebox

def clickLeft():
    messagebox.showinfo("마우스", "왼쪽 버튼이 클릭")

window = Tk()

window.bind("<Button-1>", clickLeft)

window.mainloop()