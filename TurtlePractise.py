

def draw_circle(x,y,color,rad):
    var1.penup()
    var1.goto(x, y)
    var1.pendown()
    var1.begin_fill()
    var1.fillcolor(color)
    var1.circle(rad)
    var1.end_fill()
    var1.penup()
    var1.home()

import turtle
var1 = turtle.Turtle()
var1.color("white")
#var1.shape("turtle")
screen1 = turtle.Screen()
screen1.bgcolor("black")
screen1.title("Practise of Turtle")
draw_circle(0,-50,"red",50)
draw_circle(200,200,"green",50)

'''
#Draw olymphics logo
import turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.width(6)

# Draw the Olympic rings
colors = ["blue", "black", "red", "yellow", "green"]
positions = [(-120, 0), (0, 0), (120, 0), (-60, -80), (60, -80)]

for color, (x, y) in zip(colors, positions):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.circle(80)

screen.mainloop()

var2 = turtle.Turtle()

#screen1.bgpic("Flowers1.gif")
screen1.bgpic()
#Change turtle direction or facing
var1.setheading(90)
#var1.forward(100)
#var1.backward(40)
#var1.right(45)
#var1.forward(100)
#Square shape
var2.begin_fill()
var2.fillcolor("blue")
#for i in range(4):
#    var2.forward(100)
 #   var2.left(90)
#var2.write("Fatima")
#var2.end_fill()
var2.circle(50,extent=180)
var1.circle(100)
var1.begin_fill()
var1.fillcolor("green")
var1.circle(40, steps=3)
var1.circle(60, steps=5)
var1.circle(80, steps=8)
var1.end_fill()
var1.penup()
var1.goto(200, 0)
var1.pendown()
var1.circle(50,steps=3)
'''

screen1.mainloop()