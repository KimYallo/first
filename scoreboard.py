from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 230)
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"{self.l_score} : {self.r_score}", align=ALIGNMENT, font=FONT)
