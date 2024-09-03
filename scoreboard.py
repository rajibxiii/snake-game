from turtle import Turtle
ALIGHTMENT = "center" # written like this. because, in future we can change these from here. no need to find things in the code below
SCOREFONT = ("Courier", 18, "normal")
TEXTFONT = ("Courier", 20, "bold")

class Scoreboard (Turtle):
    def __init__ (self, speedChosen):
        super().__init__()
        self.currentScore = 0
        self.speed = speedChosen
        self.speeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score (self): # writes score
        self.write(f"SCORE: {self.currentScore}", align=ALIGHTMENT, font=SCOREFONT)

    def addScore (self):
        self.currentScore += self.speeds[self.speed-1]
        self.clear() # clearing previous score
        self.update_score()
    
    def gameOver (self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGHTMENT, font=TEXTFONT)