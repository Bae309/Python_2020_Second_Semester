aa=[]
bb=[]
value=0

for i in range(0,200):
    aa.append(value)
    value=value+3

for i in range(0,200):
    bb.append(aa[199-i])

print("bb[0]= %d, bb[199]= %d" % (bb[0],bb[99]))

print('\n\n')

for i in range(0,200):
    print('%d' % aa[i], end=' ')

print('\n\n')

for i in range(0,200):
    print('%d' % bb[i], end=' ')
    
