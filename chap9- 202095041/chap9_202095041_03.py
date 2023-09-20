def func1():
    global a
    a=10
    print("func1()==> a : %d" % a)

def func2():
    print("func2()==> a : %d" % a)

a=20

##main

func1()
func2()
    
