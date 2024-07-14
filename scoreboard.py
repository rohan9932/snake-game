from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Chalkboard SE", 30, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.score = 0
        self.scoreboard()

    def scoreboard(self):
        self.goto(x=0, y=260)
        self.write(f"Score: {self.score}", move=True, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.home()
        self.write("Game Over!", align=ALIGNMENT, font=FONT)