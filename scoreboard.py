from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.color("white")
        self.write(arg = f"Score : {self.score}",align = "center", font = ("Arial", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg = "GAME OVER!", align= "center", font=("Arial", 24, "normal"))
