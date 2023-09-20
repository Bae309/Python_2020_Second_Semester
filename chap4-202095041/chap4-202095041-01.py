## 변수 선언
'''money, c500, c100, c50, c10 = 0,0,0,0,0

money = int(input("교환할 돈을 입력하세요?"))

c500 = money // 500
money = money % 500    ##money%=500

c100 = money//100
money = money % 100   ##money%=500

c50 = money//50
money = money % 50   ##money%=500

c10 = money//10
money = money % 10   ##money%=500

print("\n\n 500원 짜리 ==> %d" % c500)
print(" 100원 짜리 ==> %d" % c100)
print(" 50원 짜리 ==> %d" % c50)
print(" 10원 짜리 ==> %d" % c10)
print("나머지 | 잔돈 ==> %d" % money)'''

money, c50000, c10000, c1000, c500 = 0,0,0,0,0

money = int(input("교환할 돈을 입력하세요?"))

c50000 = money // 50000
money = money % 50000    ##money%=50000

c10000 = money // 10000
money = money % 10000   ##money%=10000

c1000 = money // 1000
money = money % 1000   ##money%=1000

c500 = money // 500
money = money % 500   ##money%=500

print("\n\n 50000원 짜리 ==> %d개" % c50000)
print(" 10000원 짜리 ==> %d개" % c10000)
print(" 1000원 짜리 ==> %d개" % c1000)
print(" 500원 짜리 ==> %d개" % c500)
print(" 나머지 | 잔돈 ==> %d원" % money)


