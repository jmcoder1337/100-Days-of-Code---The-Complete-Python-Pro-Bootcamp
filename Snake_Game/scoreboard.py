from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def post_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.post_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)