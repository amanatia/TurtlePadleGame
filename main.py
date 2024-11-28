from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

#Screen setup 
screen = Screen()
screen.bgcolor("black")
screen.setup(height= 600, width= 800)
screen.title("Pong")

screen.tracer(0)

l_paddle = Paddle((-350, 0)) #(x, y)

r_paddle = Paddle((350, 0)) #(x, y)

ball = Ball()

score = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")



game_is_on = True

while game_is_on:
    
    
    time.sleep(0.1) #slow down the ball movement
    
    ball.move()
    screen.update()
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        
    if ball.xcor() > 400:
        ball.reset()       
        score.l_point()
        
    if ball.xcor() < -400:
        ball.reset()
        score.r_point()
        
    
      
        

screen.exitonclick()