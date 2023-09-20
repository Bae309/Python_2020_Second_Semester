def para_func(*para):
    result=0
    for num in para:
        result=result+num

    return result

def func1(**para):
    for k in para.keys():
        print("%s---> %d" % (k,para[k]))

hap=0

hap=para_func(10,20,20,30,40,50)
print("hap= %d" % hap)

hap=para_func(10,20,30,10,20,20,30,40,50,10,20,20,30,40,50)
print("hap= %d" % hap)

hap=para_func(10)
print("hap= %d" % hap)

func1(트와이스=9, 소녀시대=7, 걸스데이=4, 블랙핑크=4)

