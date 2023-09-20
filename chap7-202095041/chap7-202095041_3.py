aa=[]
bb=[]

value=0

for i in range(0,200):
    aa.append(value)
    value=value+3
    
bb=aa.copy()
bb.reverse()

for i in range(0,200):
    print("%d" % aa[i], end=" ")

print(" ")

print("bb[0]=%d, bb[199]=%d" % (bb[0],bb[199]))
