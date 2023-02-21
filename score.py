from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.highscore = ""

    def track_score(self, num):
        self.clear()
        self.pendown()
        self.write(f"Score : {num}   High Score: {self.highscore}", False, align="center", font=('Arial', 18, 'normal'))

    def highscore_change(self, num):
        if num > int(self.highscore):
            self.highscore = str(num)

    def game_over(self, num):
        self.clear()
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER\nSCORE: {num}\ngame is restarting", False, align="center", font=('Arial', 18, 'normal'))
        self.goto(0, 275)

    def getting_highscore(self):
        with open("highscore.txt") as file:
            self.highscore = file.read()

    def setting_highscore(self):
        with open("highscore.txt", 'w') as file:
            file.write(self.highscore)

    def score_process(self, num):
        self.getting_highscore()
        self.highscore_change(num)
        self.setting_highscore()
