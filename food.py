from turtle import Turtle
import random

shapes = ("square", "circle", "triangle")
colors = ("red", "green", "blue", "yellow")
# Food class will inherit from Turtle class and have additional functionalities

class Food(Turtle):
    def __init__(self):
        super().__init__()
        # self.shape(random.choice(shapes))
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)   # default len and wid is 20, so stretch by 0.5 makes it 10.
        # self.color(random.choice(colors))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.shape(random.choice(shapes))
        self.color(random.choice(colors))
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 260)
        self.goto(rand_x, rand_y)