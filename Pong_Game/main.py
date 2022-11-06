from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
PADDLE_R_XPOS = 350
PADDLE_R_YPOS = 0
PADDLE_L_XPOS = -350
PADDLE_L_YPOS = 0

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong: The Famous Arcade Game')
screen.tracer(0)

paddle_r = Paddle((PADDLE_R_XPOS, PADDLE_R_YPOS))
paddle_l = Paddle((PADDLE_L_XPOS, PADDLE_L_YPOS))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_l.up, 'w')
screen.onkey(paddle_l.down, 's')
screen.onkey(paddle_r.up, 'Up')
screen.onkey(paddle_r.down, 'Down')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle.
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses the ball.
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    # Detect when left paddle misses the ball.
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()



screen.exitonclick()