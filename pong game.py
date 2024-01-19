import turtle
a_wins = 0
b_wins = 0
# Set up the screen
w = turtle.Screen()
w.title(" Pong game ")
w.bgcolor("black")
w.setup(width=900, height=600)
w.tracer(0)
# Score
score_a = 0
score_b = 0
score_lim = 11
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed()
paddle_a.color("blue")
paddle_a.shape("square")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=8, stretch_len=1)
# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed()
paddle_b.color("red")
paddle_b.shape("square")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=8, stretch_len=1)
paddle_a_speed = 60
paddle_b_speed = 60
# Ball
ball = turtle.Turtle()
ball.speed()
ball.shape("circle")
ball.color("yellow")
ball.goto(0, 0)
ball.penup()
ball.dy = 0.6
ball.dx = 0.6
# Pen
pen = turtle.Turtle()
pen.speed()
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0, 240)
pen.write("Player A: 0  Player B: 0", align="center", font=("Arial", 26, "italic"))
# Win
win = turtle.Turtle()
win.speed()
win.penup()
win.color("white")
win.hideturtle()
win.goto(0, 0)
# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += paddle_a_speed
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= paddle_a_speed
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += paddle_b_speed
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= paddle_b_speed
    paddle_b.sety(y)
turtle.listen()
turtle.onkey(paddle_a_up, "Up")
turtle.onkey(paddle_a_down, "Down")
turtle.onkey(paddle_b_up, "8")
turtle.onkey(paddle_b_down, "2")
# Main game loop
while 1:
    w.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Border
    if ball.ycor() > 220:
        ball.sety(220)
        ball.dy *= -1
    elif ball.ycor() < -220:
        ball.sety(-220)
        ball.dy *= -1
    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
    # Paddle
    if 340 < ball.xcor() < 350 and paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
    if -340 > ball.xcor() > -350 and paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1
    pen.clear()
    pen.write(f"Player A: {score_a}        Player B: {score_b}", align="center", font=("Arial", 26, "italic"))
    if score_a == score_lim:
        turtle.clearscreen()
        a_wins = 1
        break
    elif score_b == score_lim:
        turtle.clearscreen()
        b_wins = 1
        break
while 1:
    if a_wins:
        w.bgcolor("black")
        win.write("Player A wins", align="center", font=("Arial", 50, "italic"))
    elif b_wins:
        w.bgcolor("black")
        win.write("Player B wins", align="center", font=("Arial", 50, "italic"))