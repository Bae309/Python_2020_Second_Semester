instr,outstr=" "," "
count,i=0,0

instr=input("input=")
count=len(instr)

for i in range(0,count):
    outstr=outstr+instr[count-(i+1)]

print("first=%s, second=%s" % (instr,outstr))
