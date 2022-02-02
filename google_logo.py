'''blue=4285F4
red=EA4335
yellow=FBBC05
green=34A853'''
from turtle import *
Turtle(visible=False)
# speed(0)
hideturtle()
# bgcolor('#000000')
# pensize(1)
color=['#4285F4','#EA4335','#FBBC05','#34A853']

#blue color
pencolor(color[0])
forward(185)
right(90)
circle(-200,60)

#green color
pencolor(color[3])
circle(-200,100)

#yellow color
pencolor(color[2])
circle(-200,50)

#red color
fillcolor(color[1])
begin_fill()
pencolor(color[1])
circle(-200,90)
right(110)
forward(60)
right(60)
circle(140,90)
right(110)
forward(66)
end_fill()

#yellow fill
pencolor(color[2])
fillcolor(color[2])
begin_fill()
right(180)
forward(66)
right(70)
circle(140,30)
right(59)
forward(73)
right(110.225)
circle(-200,48)
end_fill()

#green color
fillcolor(color[3])
right(101.4)
forward(66)
right(70)
circle(140,30)
begin_fill()
pencolor(color[3])
circle(140,95)
right(59)
forward(70)
right(108)
circle(-200,99)
right(69)
forward(77)
end_fill()

#blue color fill
fillcolor(color[0])
right(120.58)
circle(140,96)
begin_fill()
pencolor(color[0])
# right(59)
# forward(70)
# right(108)
circle(140,45)
left(118.5)
forward(116)
right(90.5)
forward(60)
right(89.8)
forward(185)
right(90)
circle(-200,61)
right(72)
forward(70)
end_fill()
done()
