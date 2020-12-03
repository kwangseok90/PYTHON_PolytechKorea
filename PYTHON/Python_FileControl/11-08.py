inFp, outFp = None, None

inStr = ""

fName = ""

fName = input("소스파일 입력: ")
inFp = open(fName, "r", encoding="utf-8")
fName = input("타깃 파일 입력: ")
outFp = open(fName, "w", encoding="utf-8")

inList = inFp.readlines()

for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()

print("---파일이 정상적으로 복사되었습니다.-----")