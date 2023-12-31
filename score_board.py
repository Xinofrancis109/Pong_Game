import turtle as t

class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.play1 = 0
        self.play2 = 0
        self.color("white")
        # self.update()

    def update(self):
        self.setheading(90)
        self.forward(250)
        self.hideturtle()
        self.color("white")
        self.write(f'{self.play1}:{self.play2}', align="center", font=("Arial", 35, "normal"))

    def add1(self):
        self.play1 += 1
        self.update()

    def add2(self):
        self.play2 += 1
        self.update()
