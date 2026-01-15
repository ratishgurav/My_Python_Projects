from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.highscore = None
        self.hs = None
        self.score = 0
        self.readhs()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.highscore<self.score:
            self.highscore=self.score
            self.writehs()
        self.score=0


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def readhs(self):
        self.hs = open("data.txt")
        self.highscore = int(self.hs.read())
        self.hs.close()

    def writehs(self):
        with open("data.txt","w") as hghs:
            hghs.write(f"{self.highscore}")


