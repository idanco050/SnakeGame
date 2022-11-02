from turtle import Turtle
class Snake:
    the_snake = []
    def __init__(self):
        for i in range(0,3):
            t = Turtle()
            t.goto(-20*i,0)
            t.shape("square")
            t.color("white")
            t.penup()
            self.the_snake.append(t)
    def move(self):
        size = len(self.the_snake)
        for i in range(0,size-1):
            self.the_snake[(size - 1)-i].goto(self.the_snake[(size - 2)-i].xcor(),self.the_snake[(size-2)-i].ycor())
        self.the_snake[0].forward(20)
    def up(self):
        self.the_snake[0].setheading(90)
    def down(self):
        self.the_snake[0].setheading(270)
    def right(self):
        self.the_snake[0].setheading(0)
    def left(self):
        self.the_snake[0].setheading(180)
    def add_part(self):
        size = len(self.the_snake)
        t = Turtle()
        t.goto(self.the_snake[size-1].xcor()-20,self.the_snake[size-1].ycor())
        t.shape("square")
        t.color("white")
        t.penup()
        self.the_snake.append(t)



