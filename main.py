import time
from turtle import Turtle,Screen
import random
from snake import Snake
from food import Food
from game_board import GameBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Game")
screen.tracer(0)
f = Food()
s = Snake()
g = GameBoard()
flag = True
screen.listen()
screen.onkey(s.up,"Up")
screen.onkey(s.down,"Down")
screen.onkey(s.right,"Right")
screen.onkey(s.left,"Left")
while flag:

       g.is_apple_eaten(snake = s, food = f)
       screen.update()
       time.sleep(0.1)
       s.move()
       if g.error_check(s):
           g.score_board.clear()
           g.score_board.goto(0,0)
           g.score_board.write("GAME OVER",font=("Verdana", 15, "normal"),align="center")
           print("you lose !!!")
           flag = False




screen.exitonclick()