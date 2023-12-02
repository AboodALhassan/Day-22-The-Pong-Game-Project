from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)
        self.penup()
        self.setheading(90)
        self.goto(x, y)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)