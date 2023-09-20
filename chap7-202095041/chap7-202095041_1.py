aa=[0,0,0,0]
hap=0

for i in range(0,10):
    aa.append(0)


for i in range(0,10):
    aa[i]=int(input(str(i+1)+" 번째숫자입력 :"))

for i in range(0,10):
    hap=hap+aa[i]

print("합계===> %d" % hap)

aa=[]
bb=[10,20,30]
cc=['파이썬','물리학','배성윤']
dd=[10,20,'물리학']
