#변수선언부분

inStr, outStr = "",""

count,i=0,0


#매안코드 부분
inStr = input("문자 입력해주세요. ")
count = len(inStr)

for i in range(0, count):
    outStr += inStr[count - (i+1)]

print("내용 거꾸로 출력 : %s" % outStr)