from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(0,780)
        self.setheading(270)
        for i in range(16):
            self.pendown()
            self.forward(50)
            self.penup()
            self.forward(50)
        x=-200
        for j in range(2):
            self.hideturtle()
            self.penup()
            self.pencolor("white")
            self.goto(x,300)
            x+=400
            self.pendown()

    def score_p1(self,i):
        self.goto(-200,300)
        self.write(f"{i}", False, align= "center", font= ('Arial', 40, "bold"))
    
    def score_p2(self,x):
        self.goto(200,300)
        self.write(f"{x}", False, align= "center", font= ('Arial', 40, "bold"))