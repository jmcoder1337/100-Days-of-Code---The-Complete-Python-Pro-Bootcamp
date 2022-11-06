from turtle import Turtle, position

PADDLE_R_WIDTH = 20
PADDLE_R_HEIGHT = 100
PADDLE_R_XPOS = 350
PADDLE_R_YPOS = 0
PADDLE_L_XPOS = -350
PADDLE_L_YPOS = 0

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
