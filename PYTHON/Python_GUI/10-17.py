from tkinter import *

Window = Tk()

mainMenu = Menu(Window)
Window.config(menu=mainMenu)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기")
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=Window.quit)

Window.mainloop()