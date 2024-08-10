from turtle import *


#we want to paint a house

#step 1:  draw a square

width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(75)
color("black")
left(90)
forward(100)
right(90)
forward(55)
right(90)
forward(100)

penup()
goto(200, 200)
pendown()

color("purple")
right(150)
forward(200)
left(120)
forward(200)

penup()
goto(20, 110)
pendown()

color("purple")
right(150)
forward(60)
right(90)
forward(50)
right(90)
forward(60)
right(90)
forward(50)


penup()
goto(130, 110)
pendown()

right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)
right(90)
forward(50)