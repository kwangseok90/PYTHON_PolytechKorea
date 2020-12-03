inFp, outFp = None,  None

inStr, outStr = "", ""


#암호화 또는 암호 해석 코드

i = 0
secu = 0

secuYN = input("1.암호화 2.암호해석 선택: ")
inFname = input("입력 파일명: ")
outFname = input("출력파일명: ")

if secuYN == "1":
    secu = 100
elif secuYN == "2":
    secu = -100


inFp = open(inFname, 'r', encoding='UTF-8')
outFp = open(outFname, 'w', encoding='UTF-8')

while True:
    inStr = inFp.readline()
    if not inStr:
        break

    outStr = ""
    for i in range(0, len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum+=secu
        ch2 = chr(chNum)
        outStr+=ch2

    outFp.write(outStr)


outFp.close()
inFp.close()
print("%s --> %s 변환 완료. " %(inFname, outFname))



