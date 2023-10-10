import turtle as t 
import random as random
tim=t.Turtle()
tim.speed("fastest")
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colors=(r,g,b)
    return colors

def first(num):
    print("This program draws squares of many colors.")
    while not num.isdigit():
        print("\nThe number must be an integer and at least 1.\nPlease try again!!!")
        num=input("Enter the number of squares to draw:")

    def square():
        for i in range(4):
            tim.forward(90)
            tim.right(90)
    def draw(num):
        angle=int(360/num)
        for i in range(int(360/angle)):
            tim.fillcolor(random_color())
            tim.begin_fill()
            square()
            tim.end_fill() 
            tim.setheading(tim.heading()+angle)
    draw(int(num))               

first(input("Enter the number:"))    
def second(num):
    print("This program draws concentric circles of many different colors.")
    num1=float(num)-int(num)
    while num1:
       print("\nThe number must be an integer and at least 1.\nPlease try again!!!")
       num=input("Enter the number of squares to draw:")
    num=int(num)
    r=int(input("Enter the radius (>=50, <=200) of the largest circle:"))
    while not 50<=r<=200:
        print("The radius must be an integer between 50 and 300.")
        print("Try again.")
    tim.forward(r)
    tim.left(90)
    for circle in range(num,0,-1):
        tim.begin_fill()
        tim.color(random_color())
        tim.circle(r*circle/num)
        tim.end_fill()
        tim.left(90)
        tim.forward(r/num)
        tim.right(90)

second(input("Enter the number of circle to draw:"))
screen=t.Screen()
screen.exitonclick()

