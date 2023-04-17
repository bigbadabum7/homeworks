from turtle import *

#we wont to paint a hose
speed(7)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square
#drowing a door

#door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#gadatana
penup()
goto(200,200)
pendown()

#saxuravi
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#fanjara1
penup()
goto(200,100)
pendown()

color("green")
begin_fill()
right(150)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#fanjara2
penup()
goto(0,100)
pendown()

color("green")
begin_fill()
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#kvadrati kvadratshi
#1
penup()
goto(-100,0)
pendown()

color("black")
begin_fill()
backward(100)
right(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
end_fill()

#2

penup()
goto(-100,-100)
pendown()

color("red")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
end_fill()

#end

penup()
goto(+200,-200)
pendown()


forward(200)
exitonclick()
