from turtle import Turtle
import random

class food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        # create food at random place
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)

        self.goto(random_x, random_y)
