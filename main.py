#Nigeria Flag Using Python Created By CyberRide
import colorsys
import turtle
from turtle import *

wn = turtle.Screen()
wn.bgcolor("gold")

turtle = turtle.Turtle()

turtle.speed(2)
turtle.penup()
turtle.shape("turtle")

setup(700, 500)
def draw(x,y,length,width,color):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
def green():
    x=-350
    y = 250
    color = "green"
    draw(x,y,500,270,color)
def white():
    x=-150
    y=250
    color = "white"
    draw(x,y,500,270,color)
def green2():
    x=100
    y=250
    color = "green"
    draw(x,y,500,270,color)
def cy():
    turtle.penup()
    turtle.goto(-200, -100)
    turtle.pencolor("white")
    turtle.write("Created by CyberRide", font=("Helevetica", 34, "bold"))
def cys():
    turtle.penup()
    turtle.goto(-150, 1)
    turtle.pencolor("white")
    turtle.write("Nigeria Flag", font=("Helevetica", 34, "bold"))
def happy():
    turtle.penup()
    turtle.goto(-130, -145)
    turtle.pencolor("green")
    turtle.write("🄷🄰🄿🄿🅈", font=("Helevetica", 54, "bold"))
def independence():
   turtle.penup()
   turtle.goto(-150, -165)
   turtle.pencolor("green")
   turtle.write("🄸🄽🄳🄴🄿🄴🄽🄳🄴🄽🄲🄴", font=("Helevetica", 28, "bold"))
def day():
   turtle.penup()
   turtle.goto(-90, -225)
   turtle.pencolor("green")
   turtle.write("🄳🄰🅈", font=("Helevetica", 54, "bold"))
    
def coat():
    wn.addshape("f.gif")
    turtle.shape("f.gif")
    penup()
    turtle.goto(-20, 25)
    pendown()
    wn.mainloop()
cys() 
cy()
green()
white()
green2()
happy()
independence()
day()
coat()



turtle.hideturtle()
turtle.getscreen()._root.mainloop()
