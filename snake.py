from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.square_list = []
        self.create_snake()
        self.head = self.square_list[0]

    def add_square(self, position):
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        square.setpos(position)
        self.square_list.append(square)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def move(self):
        for sq_num in range(len(self.square_list) - 1, 0, -1):  # start, finish, step for loop
            new_x = self.square_list[sq_num - 1].xcor()
            new_y = self.square_list[sq_num - 1].ycor()
            self.square_list[sq_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_square(self.square_list[-1].position())   # -1 gives the last element in list

    def up(self):
        if self.square_list[0].heading() == DOWN:
            return
        self.square_list[0].setheading(90)

    def down(self):
        if self.square_list[0].heading() == UP:
            return
        self.square_list[0].setheading(270)

    def right(self):
        if self.square_list[0].heading() == LEFT:
            return
        self.square_list[0].setheading(0)

    def left(self):
        if self.square_list[0].heading() == RIGHT:
            return
        self.square_list[0].setheading(180)