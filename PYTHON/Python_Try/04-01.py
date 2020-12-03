money, c500, c100, c50, c10, c1000 = 0,0,0,0,0,0

money = int(input("교환할 돈은 얼마? "))

c1000 = money // 1000
money %= 1000

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("\n1000원 짜리 ===> %d개" % c1000)
print("\n500원 짜리 ===> %d개" % c500)
print("\n100원 짜리 ===> %d개" % c100)
print("\n50원 짜리 ===> %d개" % c50)
print("\n10원 짜리 ===> %d개" % c10)
print("바꾸지 못한 잔돈 ===> %d원" % money)
