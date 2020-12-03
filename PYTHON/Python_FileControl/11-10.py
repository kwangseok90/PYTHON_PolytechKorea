inFp, outFp = None, None

inStr = ""

inFp = open("GIF/dog5.gif", "rb")
outFp = open("dog5.gif", "wb")

while True:
    inStr = inFp.readline(1)
    if not inStr:
        break
    outFp.write(inStr)


inFp.close()
outFp.close()

print("------이전 파일 정상적 복사되었습니다. --------")