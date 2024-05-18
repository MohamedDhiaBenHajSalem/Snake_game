from turtle import Turtle

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = 0
        self.read_highscore()
        self.penup()
        self.color("white")
        self.goto(x=0,y=260)
        self.write(f"Score:{self.current_score} high score {self.high_score}",align="center",font=("Arial",24,"normal"))



    def score_counting (self):
        self.clear()
        self.current_score+=1
        self.write(f"Score:{self.current_score} high score {self.high_score}", align="center")
    def reset_score(self):
        self.clear()
        self.current_score=0
        self.write(f"Score:{self.current_score} high score {self.high_score}", align="center")

    def gameover(self):

        self.goto(0,0)
        self.write("GAME OVER",align="center")


    def high_scoreupdate(self):
        if self.current_score >self.high_score:
            self.high_score=self.current_score
            with open("highscore.txt","w") as score_directory :
                score_directory.write(str(self.high_score))

        self.reset_score()

    def read_highscore(self):
        with open("highscore.txt","r") as score_directory:
            self.high_score=int(score_directory.read())
