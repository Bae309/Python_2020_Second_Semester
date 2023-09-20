'''i,hap=0,0

for i in range(2,101,2) :
    hap=hap+i
    print("i=%d" %i, end=" ")

print("\n1부터 100까지의 합은 = %d" % hap)'''

i,hap = 0,0
num1,num2,num3=0,0,0

num1=int(input("시작값="))
num2=int(input("끝값="))
num3=int(input("증감값="))

for i in range(num1,num2+1,num3) :
    hap=hap+i

print("%d에서 %d까지 %d씩 증가(감소)시킨 값의 합계 = %d" %(num1, num2, num3, hap))
