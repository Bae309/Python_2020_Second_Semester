import random

def getnumber():
    return random.randrange(1,46)

lotto=[]
num=0

##main

print("=== 로또 번호를 추첨합니다. ===\n")

for i in range(0,5):
    lotto=[]
    while True:
        num=getnumber()

        if lotto.count(num)==0:
            lotto.append(num)

        if len(lotto)>=6:
            break

    print("추첨된 로또번호 ===>",end = ' ')

    lotto.sort()

    for i in range(0,6):
        print("%d " % lotto[i], end="")
    print()
