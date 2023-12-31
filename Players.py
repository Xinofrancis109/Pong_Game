import turtle as t


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.go_up()
        self.go_down()
        self.setheading(90)
        self.shapesize(stretch_len=4, stretch_wid=0.8)

    def direction(self, x, y):
        self.goto(x, y)

    def go_up(self):
        self.forward(40)

    def go_down(self):
        # p_one.setheading(270)
        self.backward(40)



# class Comp(Player):
#
# p_one = t.Turtle()
# p_one.shape("square")
# p_one.penup()
# p_one.setheading(90)
# p_one.shapesize(stretch_wid=0.5, stretch_len=2.5)
# p_one.goto(x=-430, y=0)
