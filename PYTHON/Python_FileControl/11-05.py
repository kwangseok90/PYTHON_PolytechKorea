import os

inFp = None
fName, inList, inStr = "", [], ""

fName = input("파일명 입력: ")



if os.path.exists(fName):
    inFp = open(fName, 'r')

    inList = inFp.readlines()

    for inStr in inList:
        print(inStr, end="")

    inFp.close()
else:
    print("%s 파일이 없습니다."%fName)