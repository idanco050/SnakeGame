from turtle import Turtle
import random
class Food:
    apple = Turtle()
    def __init__(self):
        self.apple.penup()
        self.apple.shape("circle")
        self.apple.color("blue")
        self.apple.goto(random.randint(-250,250),random.randint(-250,250))
    def move(self):
        self.apple.goto(random.randint(-250, 250), random.randint(-250, 250))
