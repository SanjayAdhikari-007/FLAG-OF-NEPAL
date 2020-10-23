import turtle

# Initialize and Speed.
scr = turtle.Screen()
root = turtle.Turtle()
# Speed 10,0(max) and 1(Slowest),You can put values between 0-10.
root.speed(6)

# BAckground Color name(hex code) : Mintcream.
root.getscreen().bgcolor('#F5FFFA')

# Title of program.
root.getscreen().title("NEPAL FLAG")

# Pen size. 
root.pensize(10)

# Hex code for blue color.
root.color("#003893")

# Move the pen without writing.
root.penup()
root.bk(200)
root.goto(-200, -200)

# Start writing.
root.pendown()
root.goto(-200, 250)

# Start filling with Crimson color.
root.begin_fill()
root.fillcolor("#DC143C")
root.rt(30)
root.fd(400)
root.setheading(180)
root.fd(250)
root.setheading(0)
root.rt(30)
root.fd(400)
root.setheading(180)
root.fd(442.81)
root.setheading(0)

# Stop filling.
root.end_fill()


# Start drawing Moon and Sun.
root.goto(-200, 250)  
root.pensize(2)
root.color("black")
root.penup()
root.rt(80)
root.fd(130)
root.rt(-20)
root.pendown()
root.begin_fill()
root.fillcolor("#FFFFFF")
root.circle(80, 130)
root.setheading(180)
root.lt(60)
root.circle(-45, 60)
root.setheading(90)
root.rt(75)
for i in range(8):
	root.fd(12)
	root.lt(160)
	root.fd(20)
	root.rt(150)
root.setheading(180)
root.circle(-45, 60)
root.end_fill()

root.color("black")
root.penup()
root.goto(-200, -150)
root.setheading(0)
root.lt(30)
root.fd(130)
root.setheading(0)
root.pendown()
root.begin_fill()
root.fillcolor("#FFFFFF")
for i in range(18):
	root.rt(60)
	root.fd(30)
	root.lt(160)
	root.fd(30)
	root.rt(80)
root.end_fill()
root.hideturtle()

# Finalize.
turtle.done()
