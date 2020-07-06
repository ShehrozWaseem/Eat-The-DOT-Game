import turtle
import time
import random

delay= 0.1
score=0
hs=0

wn = turtle.Screen()
wn.title("EAT THE DOT")
wn.bgcolor("green")
wn.setup(width=600 , height=600)
wn.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,100)
head.direction = "stop"

dot=turtle.Turtle()
dot.speed(0)
dot.shape("circle")
dot.color("red")
dot.penup()
dot.goto(0,0)
dot.direction = "stop"

body=[]

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write( "Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

while True:
    wn.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for j in body:
            j.goto(1000,1000)
        body.clear()

        score= 0
        delay=0.1
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score , hs), align="center",font=("Courier", 24, "normal"))
    
    if head.distance(dot) < 20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        dot.goto(x,y)
        
        nbody=turtle.Turtle()
        nbody.speed(0)
        nbody.shape("square")
        nbody.color("grey")
        nbody.penup()
        body.append(nbody)

        delay -=0.001

        score +=10

        if score > hs:
            hs=score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score , hs), align="center",font=("Courier", 24, "normal"))
        
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)

    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
        
    move()

    for j in body:

        if j.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for j in body:
                j.goto(1000,1000)
            body.clear()

            score=0

            delay=0.1
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score , hs),
                  align="center",font=("Courier", 24, "normal"))
            
    time.sleep(delay)

wn.mainloop()
