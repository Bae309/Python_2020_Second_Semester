i, dan = 0,0

#dan = int(input("dan input="))

for i in range(2,10,1):
    print("*** %d단 ***" % i)
    for k in range(1,10,1):
        print("%d X %d = %3d" %(i,k,k*i))
