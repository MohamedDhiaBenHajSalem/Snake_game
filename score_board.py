from turtle import Turtle

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.color("white")
        self.goto(x=0,y=260)
        self.write(f"Score:{self.current_score}",align="center",font=("Arial",24,"normal"))


    def score_counting (self):
        self.clear()
        self.current_score+=1
        self.write(f"Score:{self.current_score}", align="center")
    def reset_score(self):
        self.clear()
        self.current_score=0
        self.write(f"Score:{self.current_score}", align="center")