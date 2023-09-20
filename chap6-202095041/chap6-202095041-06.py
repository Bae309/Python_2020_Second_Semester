hap,a,b =0,0,0

while True :
    a=int(input("첫번째 수 ="))
    if a==0:
        break
    b=int(input("두번째 수 ="))
    hap=a+b
    print("%d + %d = %d" % (a,b,hap))


print("0을 입력해서 반복문을 벗어납니다.")

 #elif (ch=="$"):
     #break
    

hap,a,b =0,0,0

for a in range(1,101,1):
    hap=hap+a


    if hap>=1000:
        break

print("1~100합계에서 100이 넘은 숫자=%d, 합계=%d" % (a,hap))


hap,i=0,0

for i in range(1,101):
    if i%3==0:
        continue
    hap=hap+i

print("1~100중에서 3의 배수를 뺀 합계 : %d" % hap)
