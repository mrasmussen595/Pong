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

    def score_write(self,p1, p2):
        self.clear()
        self.penup()
        self.goto(-100,200)
        self.pencolor("white")
        self.pendown()
        self.write(p1, False, align= "center", font= ('Arial', 40, "bold"))
        self.penup()
        self.goto(100,200)
        self.pencolor("white")
        self.pendown()
        self.write(p2, False, align= "center", font= ('Arial', 40, "bold"))
    
  