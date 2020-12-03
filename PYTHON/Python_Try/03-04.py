sel =  int(input("입력 진수 결정(16/10/8/2) "))
num = input("값 입력: ")



if sel == 16:
    num10 = int(num, 16)
if sel == 10:
    num10 = int(num, 10)
if sel == 8:
    num10 = int(num, 8)
if sel == 2:
    num10 = int(num,2)

if sel != 16 | 10 | 8 | 2:
    print("(16/10/8/2) 만 됩니다.")
    exit()


print("16진수 ---> " , hex(num10)) #16진수
print("10진수 ---> ", num10) #10진수
print("8진수  ---> ", oct(num10)) #8진수
print("2진수  ---> ", bin(num10)) #2진수
