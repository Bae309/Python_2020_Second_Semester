## 함수 선언 부분 ##

def para_func(v1=0,v2=0,v3=0,v4=0,v5=0,v6=0,v7=0,v8=0,v9=0,v10=0):
    result=0
    result=v1+v2+v3+v4+v5+v6+v7+v8+v9+v10
    return result

'''def para_func(v1,v2):
    result=0
    result=v1+v2
    return result

def para3_func(v1,v2,v3):
    result=0
    result=v1+v2+v3
    return result'''

hap=0

##main

hap=para_func(10,20)
print("hap= %d" % hap)

hap=para_func(10,20,30)
print("hap= %d" % hap)

hap=para_func(10)
print("hap= %d" % hap)
