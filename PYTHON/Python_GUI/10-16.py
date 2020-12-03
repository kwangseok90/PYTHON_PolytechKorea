from tkinter import *
from tkinter import messagebox

def keyE(event):
    messagebox.showinfo("키보드 이밴트", "눌린키 : " + str(event.keycode))

window = Tk()
window.bind("<Key>", keyE)

window.mainloop()