#Import the required libraries for turtle graphics
import turtle, random, time

#set up screen with specific dimensions, title, and background color
screen = turtle.Screen()
screen.setup(600,500)
screen.title("Turtle Race")
screen.bgcolor("lavender")

#set up turtle for drawing elements like the race track and starting/finish lines
t = turtle.Turtle()
t.shape("arrow")
t.color("black")
t.penup()
t.goto(-50,150)
t.write("Turtle Race", font=("Arial",16))

#finish line
t.goto(200,100)
t.write("Finish")
t.pendown()
t.begin_fill()
for x in range(2):
    t.forward(20)
    t.right(90)
    t.forward(250)
    t.right(90)
t.end_fill()
t.penup()

#race track
y_pos = 100
for x in range(6):
    t.goto(-200,y_pos)
    t.pendown()
    t.forward(400)
    y_pos = y_pos - 50
    t.penup()

#starting line
t.penup()
t.goto(-200,100)
t.write("Start")
t.pendown()
t.begin_fill()
for x in range(2):
    t.forward(20)
    t.right(90)
    t.forward(250)
    t.right(90)
t.end_fill()
t.penup()

#Hide the main turtle before starting the race
t.ht()    

#Create and position turtles for each participant in the race
#Turtle1
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("red")
t1.penup()
t1.goto(-200,75)
t1.pendown()

#Turtle2
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("orange")
t2.penup()
t2.goto(-200,25)
t2.pendown()

#Turtle3
t3 = turtle.Turtle()
t3.shape("turtle")
t3.color("yellow")
t3.penup()
t3.goto(-200,-25)
t3.pendown()

#Turtle4
t4 = turtle.Turtle()
t4.shape("turtle")
t4.color("blue")
t4.penup()
t4.goto(-200,-75)
t4.pendown()

#Turtle5
t5 = turtle.Turtle()
t5.shape("turtle")
t5.color("violet")
t5.penup()
t5.goto(-200,-125)
t5.pendown()

#pause the code for 3 sec before starting the race
time.sleep(3) 

#moves turtle alternately and randomly by 1 to 5 
for x in range(130):
    t1.forward(random.randint(1,5))
    t2.forward(random.randint(1,5))
    t3.forward(random.randint(1,5))
    t4.forward(random.randint(1,5))
    t5.forward(random.randint(1,5))

#Finish the turtle graphics
turtle.done()