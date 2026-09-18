from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.FONT = ("Arial", 24 ,"normal")
        self.ALIGNMENT = "center"

    def initScoreboard(self):
        self.goto(0,260)
        self.write(f"Score : 0", align= self.ALIGNMENT, font= self.FONT)
    def updateScoreboard(self,score_value):
        self.goto(0,260)
        self.clear()
        self.write(f"Score : {score_value}",align=self.ALIGNMENT,font=self.FONT)
    def loseScreen(self,score_value):
        self.clear()
        self.goto(0,0)
        self.write(f"You lost with score of : {score_value}",align=self.ALIGNMENT,font=self.FONT)