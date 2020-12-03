select, answer, numStr, num1, num2 = 0,0,"",0,0

select = int(input("1. 입력한 수식 계산 2.두 수 사이의 합계 : "))

if select == 1:
    numStr = input("***수식 입력. ")
    answer = eval(numStr)
    print("%s 결과는 %5.1f입니다. " %(numStr, answer))
elif select == 2:
    num1 = int(input("첫번쨰 숫자 입력: "))
    num2 = int(input("두번쟤 숫자 입력: "))
    for i in range(num1, num2 + 1):
        answer = answer + i
    print("%d+.....+%d는 %d입니다. "%(num1, num2, answer))
else:
    print("1과 2를 선택해야 합니다. ")
