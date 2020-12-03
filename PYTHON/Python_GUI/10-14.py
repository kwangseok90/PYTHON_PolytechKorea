from tkinter import *
from tkinter import messagebox

def clickImage():
    messagebox.showinfo("마우스", "토끼에서 마우스 클릭")


window = Tk()
window.geometry("400x400")

photo = PhotoImage(file="GIF/rabbit.gif")
label1 = Label(window, image=photo)

label1.bind("<Button-1>", clickImage)

label1.pack(expand=1, anchor=CENTER)
window.mainloop()