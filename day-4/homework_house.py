from turtle import *
speed(30)
width(2)

#lets make a base
color("black")
forward(200)
left(90)
forward(200)
left(90)
color("red")
forward(200)
left(90)
color("black")
forward(200)
left(90)

#lets make a roof
color("red")
penup()
goto(200, 200)
pendown()
forward(40)
left(120)
forward(280)
left(120)
forward(280)
left(120)
forward(40)

#lets make a door with a handle
color("brown")
penup()
goto(0, 0)
pendown()
forward(75)
left(90)
forward(80)
right(90)
forward(50)
right(90)
forward(80)
color("black")
penup()
goto(75, 45)
pendown()
left(90)
forward(10)
right(45)
forward(5)

#lets make windows
color("brown")
penup()
goto(75, 110)
pendown()
left(135)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)

penup()
goto(175, 110)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)

#lets make a floor
penup()
goto(-400, 0)
pendown()
color("green")
right(90)
forward(800)



#making a base of house 2
penup()
goto(-400, 0)
pendown()
color("purple")
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)

#making a door of house 2
forward(50)
color("purple")
left(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)

#making a roof of house 2
penup()
goto(-250, 150)
pendown()
color("blue")
right(150)
forward(150)
left(120)
forward(150)

#making a door handle of house 2
penup()
goto(-350, 30)
pendown()
right(240)
color("black")
forward(10)

#making a first windown for house 2
penup()
goto(-350, 80)
pendown()
color("brown")
left(180)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)

#making a second window for house 2
penup()
goto(-300, 120)
pendown()
color("brown")
left(180)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)

#making a base for house 3 (dog house)
penup()
goto(-400, 0)
pendown()
forward(230)
left(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

#making an entrance for the dog (house 3)
right(90)
forward(20)
right(90)
forward(20)
left(45)
forward(20)
left(45)
forward(40)
left(45)
forward(20)
left(45)
forward(20)

#making a roof for house 3
penup() 
goto(-170, 0)
pendown()
right(180)
forward(100)

left(90)
forward(20)
right(120)
forward(40)
right(60)
forward(100)
right(60)
forward(40)
right(120)
forward(20)

#remaking the floor
color("grey")
penup()
goto(-700,0)
pendown()
width(6)
color("green")
right(180)


#lets make a tower
width(2)
color("grey")
color("black")
forward(1300)
right(180)
forward(250)
right(90)
forward(400)
right(90)
forward(100)
right(90)
forward(400)

#entrance for the tower
color("grey")
right(90)
forward(30)
right(90)
forward(50)
left(90)
forward(30) 
left(90)
forward(50)

#making the a roof
color("grey")
right(90)
forward(40)
right(90)
forward(400)
left(90)
forward(20)
right(90)
forward(50)
right(90)
forward(20)
right(90)
forward(25)
left(90)
forward(20)
left(90)
forward(25)
right(90)
forward(20)
right(90)
forward(25)
left(90)
forward(20)
left(90)
forward(25)
right(90)
forward(20)
right(90)
forward(25)
left(90)
forward(20)
left(90)
forward(25)
right(90)
forward(20)
right(90)
forward(50)
right(90)
forward(20)

#remaking the floor
penup()
goto(-700,0)
pendown()
width(7)
color("green")
right(180)
forward(1400)
exitonclick()
