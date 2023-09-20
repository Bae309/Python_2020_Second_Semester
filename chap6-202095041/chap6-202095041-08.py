i,k,heartNum=0,0,0
numStr, ch, heartStr=" "," "," " # 468

numStr=input("숫자입력=")
print(' ')
i=0
ch=numStr[i]
while True:
    heartNum=int(ch)
    heartStr=" "
    for k in range(0,heartNum):
        heartStr=heartStr+"\u2665"
        k=k+1
    print(heartStr)
    i=i+1
    if(i>len(numStr)-1):
        break
    
    ch=numStr[i]
