from turtle import Turtle


class Ball(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.goto(x_pos, y_pos)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.bounce_x()

    def speed_up(self):
        if self.x_move > 0:
            self.x_move += 2
        else:
            self.x_move -= 2

        if self.y_move > 0:
            self.y_move += 2
        else:
            self.y_move -= 2
