from tkinter import *
from tkinter import messagebox

Window = Tk()

def FUNC_OPEN():
    messagebox.showinfo("메뉴선택","열기 메뉴 선택")

def func_exit():
    Window.quit()
    Window.destroy()

mainMenu = Menu(Window)
Window.config(menu=mainMenu)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=FUNC_OPEN)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

Window.mainloop()