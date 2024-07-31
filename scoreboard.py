from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Chalkboard SE", 30, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file= "data.txt", mode= "r") as data:
            self.high_score = int(data.read())
        self.up()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Prints scoreboard'''
        self.goto(x=0, y=260)
        self.clear()
        self.write(arg= f"Score: {self.score}   High Score: {self.high_score}", move=True, align=ALIGNMENT, font=FONT)

    def reset(self):
        '''Resets the scoreboard'''
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file= "data.txt", mode= "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0 # reset the scores
        self.update_scoreboard()

    def increase_score(self):
        '''Increases the score'''
        self.score += 1
        self.update_scoreboard()
