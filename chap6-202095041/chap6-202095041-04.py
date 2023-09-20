i,hap=0,0
a,b = 0,0


#for i in range(1,11,1):
#    hap = hap + i

i = 1
while i<11:
    hap=hap+i
    i=i+1

print("1부터 10까지의 합계 = %d" % hap)


while True:
    a=int(input("첫번쨰 숫자 = "))
    b=int(input("두번째 숫자 = "))
    hap=a+b
    print("%d + %d = %d" % (a,b,hap))
    
