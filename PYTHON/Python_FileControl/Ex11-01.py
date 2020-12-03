from tkinter import *
import os
import os.path


def clickListBox(evt):
    global currentDir, searchDirList
    if(dirListBox.curselection()==0):
        return
    dirName = str(dirListBox.get(dirListBox.curselection()))
    if dirName == '상위폴더':
        if len(searchDirList) == 1:
            return
        searchDirList.pop()
    else:
        searchDirList.append(currentDir+dirName+'/')
    fillListBox()


def fillListBox():
    global currentDir, searchDirList, dirLabel, dirListBox, fileListBox
    dirListBox.delete(0,END)
    fileListBox.delete(0,END)
    dirListBox.insert(END, "상위폴더")
    currentDir = searchDirList[len(searchDirList)-1]
    dirLabel.configure(text=currentDir)
    folderList = os.listdir(currentDir)
    for item in folderList:
        if os.path.isdir(currentDir + item):
            dirListBox.insert(END, item)
        elif os.path.isfile(currentDir+item):
            fileListBox.insert(END, item)
        


window = None
searchDirList = ['/']
currentDir = '/'
dirLabel, dirListBox, fileListBox = None, None, None

if __name__ == "__main__":
    window = Tk()
    window.title("폴더 및 파일 보기 목록.")
    window.geometry("300x500")
    dirLabel = Label(window, text=currentDir)
    dirLabel.pack()

    dirListBox = Listbox(window)
    dirListBox.pack(side=LEFT, fill=BOTH, expand=1)
    dirListBox.bind('<<ListboxSelect>>', clickListBox)

    fileListBox = Listbox(window)
    fileListBox.pack(side=RIGHT, fill=BOTH, expand=1)
    fileListBox.bind('<<ListboxSelect>>', clickListBox)
    window.mainloop()