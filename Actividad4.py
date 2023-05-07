from turtle import *
import time

color('red')

for a in range(20):
    forward(5)
    penup()
    forward(5)
    pendown()

stamp()

penup()
home()
sety(-100)
pendown()

c=5
for b in range(8):
    forward(c)
    penup()
    forward(c)
    pendown()
    c+=3


time.sleep(3)