import random
import turtle as t
from Players import Player
from ball import Ball
import time as tm
from score_board import Score
screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=900, height=600)
screen.tracer(0)
line = t.Turtle()
score = Score()
line.penup()
line.color("white")
line.setheading(270)
line.forward(280)
line.setheading(90)
line.pensize(5)
line.hideturtle()
for i in range(28):
    line.pd()
    line.forward(10)
    line.pu()
    line.forward(10)

ball = Ball()
r_player = Player()
r_player.direction(x=430, y=0)
l_player = Player()
l_player.direction(x=-430, y=0)
screen.listen()
screen.onkey(key="Up", fun=r_player.go_up)
screen.onkey(key="Down", fun=r_player.go_down)
screen.onkey(key="w", fun=l_player.go_up)
screen.onkey(key="s", fun=l_player.go_down)

game_on = True
while game_on:
    tm.sleep(0.07)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_player) < 50 and ball.xcor() > 400 or ball.distance(l_player) < 50 and ball.xcor() < -400:
        ball.bounce_x()
        # print("bounce")
    if ball.xcor() > 420:
        score.add1()
        ball.reset_position()
        ball.bounce_y()
    if ball.xcor() < -420:
        score.add2()
        ball.reset_position()
        ball.bounce_y()



screen.exitonclick()