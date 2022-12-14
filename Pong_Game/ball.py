from turtle import Turtle
STARTING_XCOR = 0
STARTING_YCOR = 0
BALL_INITIAL_MOVE_SPEED = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        # self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = BALL_INITIAL_MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.move_speed *= 0.9
        self.x_move *= -1

    def reset(self):
        self.move_speed = BALL_INITIAL_MOVE_SPEED
        self.goto(STARTING_XCOR, STARTING_YCOR)
        self.bounce_x()