from tkinter import *

window = Tk()

window.title("사진첩")
#window.geometry("400x400")
window.resizable(width=False, height=False)
photo1 = PhotoImage(file="../../Test_Figure/GIF/cat.gif")
photo2 = PhotoImage(file="../../Test_Figure/GIF/cat2.gif")
label1 = Label(window, image=photo1)
label2 = Label(window, image=photo2)
#label3 = Label(window, text="강아지 입니다.", font=("궁서체", 12), fg="blue")

label1.pack(side=LEFT)
label2.pack()

window.mainloop()