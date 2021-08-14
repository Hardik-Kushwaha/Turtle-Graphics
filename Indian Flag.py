from turtle import *
Turtle(visible=False)
hideturtle()
title('Happy Independence Day')

speed(8)
penup()
goto(-220,180)
pendown()
pencolor('#000080')
write('Happy Indepencence Day',font=('Cascadia code',25))

#Green Color
penup()
goto(-230,-50)
pendown()
pencolor('#138808')
fillcolor('#138808')
begin_fill()
forward(450)
right(90)
forward(100)
right(90)
forward(450)
right(90)
forward(100)
end_fill()

#White Color
pencolor('white')
forward(100) 

#orangecolor
pencolor('#FF9933')
fillcolor('#FF9933')
begin_fill()
forward(100) 
right(90)
forward(450)
right(90)
forward(100)
right(90)
forward(450)
right(90)
forward(100)
end_fill()

#Ashoka Chakra
penup()
goto(35,0)
pendown()
pencolor('#000080')
pensize(2)
for i in range(24):
    circle(40,15)
    left(90)
    forward(40)
    backward(40)
    right(90)
circle(40)

done()