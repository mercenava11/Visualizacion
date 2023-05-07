from turtle import *
import time
import math

color('purple')
penup()
setposition(-250.00, 0.00)
pendown()

lados = 3

for i in range(3):
    for a in range(lados):
        forward(100)
        left(360/lados)
    penup()
    forward(200)
    pendown()
    lados +=1

hideturtle()

time.sleep(3)



