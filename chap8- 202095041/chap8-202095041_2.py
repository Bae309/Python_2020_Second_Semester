ss=input("input=")
print("output====>", end=" ")

if ss.startswith('(')==False:
    print('(',end=" ")

print(ss,end=" ")

if ss.endswith(')')==False:
    print(')',end=" ")
