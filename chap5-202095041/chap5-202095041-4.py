import random

for i in range(1,6):
    numbers = []
    for num in range(0,6):
        numbers.append(random.randrange(0,46))

    print("생성된 리스트%d  = " % i, numbers)

#for num in range(0,10):
    #if num not in numbers :
        #print("숫자 %d는(은) 리스트에 없네요." %num)
