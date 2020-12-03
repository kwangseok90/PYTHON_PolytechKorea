outFp = None
ouStr = ""

outFp = open("file/data2.txt", "w")

while True:
    outStr = input("내용 입력: ")
    if outStr != "":
        outFp.writelines(ouStr + "\n")
    else:
        break


outFp.close()
print("-----정상적 으로 파일에 씀------")