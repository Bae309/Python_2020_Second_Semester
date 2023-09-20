import turtle

##전역 함수 부분##
num = 0 #입력받을 진수
swidth, sheight = 1000, 300 #윈도창의 폭과 넓이 
curX, curY = 0,0 #거북이의 현재 위치를 설정하는 변수


##메인 코드 부분##
if __name__ == "__main__" :
    turtle.title('거북이로 2진수 표현하기') #터틀 그래픽 준비
    turtle.shape('turtle') #터틀 모양
    turtle.setup(width = swidth + 50 , height = sheight + 50) 
    turtle.screensize(swidth,sheight)
    turtle.penup() 
    turtle.left(90) #거북이의 각도

    num = int(input("숫자를 입력하세요 : ")) #입력한 수를 이진수로 변환
    binary = bin(num)
    curX = swidth / 2
    curY = 0
    for i in range(len(binary) -2) :
        turtle.goto(curX,curY) #계산된 좌표로 거북이 이동
        if num & 1 : #숫자를 2로 변환했을 때 만해위비트가 1인지 확인
            turtle.color('red') 
            turtle.turtlesize(2)

        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num >>= 1

turtle.done() #터틀 종료
