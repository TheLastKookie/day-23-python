from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 0
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.goto(x=-290, y=270)
        self.write(arg=f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
