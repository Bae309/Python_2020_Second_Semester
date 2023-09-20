coffee=0
a=1

##함수선언부분##
def coffee_machine(button):
    print()
    print("#1. (자동으로)뜨거운 물을 준비한다.");
    print("#2. (자동으로)종이컵을 준비한다.");

    if button == 1:
        print("#3. (자동으로)보통커피를 탄다.");
    elif button ==2 :
        print("#3. (자동으로)설탕커피를 탄다.");
    elif button ==3 :
        print("#3. (자동으로)블랙커피를 탄다.");
    else:
        print("#3. (자동으로)아무거나 탄다.");

    print("#4. (자동으로)물을 붓는다.");
    print("#5. (자동으로)스푼으로 젓는다.");
    print()

##Main code##
while True :
    print()
    coffee = int(input(str(a)+" 번 손님, 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
    if coffee==100:
        break


    
    coffee_machine(coffee)
    print(str(a)+" 번 손님~ 여기 커피 있습니다.")
    a=a+1


