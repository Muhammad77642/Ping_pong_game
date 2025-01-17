import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
window=Screen()
window.bgcolor("black")
window.setup(800,600)
window.title("Ping Pong")
window.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball= Ball()
score=Scoreboard()

window.listen()
window.onkey(r_paddle.go_up, "Up")
window.onkey(r_paddle.go_down, "Down")
window.onkey(l_paddle.go_up,"w" )
window.onkey(l_paddle.go_down,"s")
speed_change=0.1
game_on=True
while game_on:
    window.update()

    time.sleep(speed_change)

    ball.goto(ball.xcor()+ball.x_move, ball.ycor()+ball.y_move)
# discovering collision between y-axes
    if ball.ycor() >= 280 or ball.ycor() <= -280 :
        ball.y_move *=-1
# discovering collision between paddles


    if (ball.xcor()>= 330 and ball.distance(r_paddle) <= 50)  :
        ball.x_move *= -1
        speed_change *= 0.6
        # ball.x_move -= 3
        # ball.y_move -= 3
    if (ball.xcor() <= -330 and ball.distance(l_paddle) <= 50 ):
        ball.x_move *= -1
        speed_change *= 0.6
      #both ways are coreect !!!!
        # ball.x_move += 3
        # ball.y_move += 3

    if (ball.xcor()> 400):
        ball.goto(0,0)
        ball.x_move*=-1
        score.left_score()
        score.score_show()
        #ball.x_move = 10
        #ball.y_move = 10
        speed_change = 0.1

    if (ball.xcor() < -400 ):
        ball.goto(0,0)
        ball.x_move*=-1
        score.right_score()
        score.score_show()
        # ball.x_move = 10
        # ball.y_move = 10
        speed_change = 0.1




window.exitonclick()
