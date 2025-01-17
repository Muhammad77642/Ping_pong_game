from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.rightscore=0
        self.leftscore=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score_show()
    def left_score(self):
        self.leftscore+=1

    def right_score(self):
        self.rightscore+=1

    def score_show(self):
        self.clear()
        self.goto(70,240)
        self.write(f"{self.rightscore}",align="center",font=("arial",42,"bold"))
        self.goto(-50,240)
        self.write(f"{self.leftscore}",align="center",font=("arial",42,"bold"))
