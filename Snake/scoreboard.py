from turtle import Turtle
FONTSTYLE = ('Courier', 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./Snake/data.txt", mode="r") as self.file:
            self.highscore = int(self.file.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", font=FONTSTYLE, align="center")
  
    def reset(self):
        if str(self.score) > str(self.highscore):
            self.highscore = self.score
            print(self.highscore)
            with open("./Snake/data.txt", mode="w") as file:
               file.write(f"{self.highscore}")
               
        self.score = 0 
        self.update_score()

        
    def add_score(self):
        self.score += 1
        self.update_score()
        
        