from turtle import Turtle

class Scoreboard (Turtle):
    def __init__ (self, speedChosen):
        super().__init__()
        self.currentScore = 0
        self.speed = speedChosen
        self.speeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.write(f"Score: {self.currentScore}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()
        
    def addScore (self):
        self.currentScore += self.speeds[self.speed-1]