import turtle
import random

myT=turtle.Turtle('arrow')
myT.speed(10)

for k in range(0,36):
    myT.right(10)
    myT.color(random.random(),random.random(),random.random())
    
    for i in range(0,6):
        myT.right(120)
        myT.forward(100)
