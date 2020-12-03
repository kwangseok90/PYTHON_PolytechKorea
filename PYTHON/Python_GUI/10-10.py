from tkinter import *

window = Tk()
window.title("축구")

window.resizable(width=False, height=False)

photo1 = PhotoImage(file="../../Test_Figure/Internet/bang.gif")
Label1 = Label(window, image=photo1)

photo2 = PhotoImage(file="../../Test_Figure/Internet/bang2.gif")
Label2 = Label(window, image=photo2)
Label3 = Label(window, text="슛 골인~~", font=("궁서체", 30), fg="green")

Label3.pack()
Label1.pack(side=RIGHT)
Label2.pack(side=LEFT)

window.mainloop()


