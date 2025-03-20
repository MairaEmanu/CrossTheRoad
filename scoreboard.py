from turtle import Turtle


FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 40, "normal")
ALIGNMENT = "center"
POSITION = (-290,270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.setposition(POSITION)
        self.color("black")
        self.update()


    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)
        self.level += 1


    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT ,font=GAME_OVER_FONT)