from snake import Snake
from food import Food
from turtle import Turtle
class GameBoard:
    score = 0
    score_board = Turtle()
    def __init__(self):
        self.score_board.hideturtle()
        self.score_board.goto(0,250)
        self.score_board.color("white")
        self.score_board.write(f"score :{self.score} ", font=("Verdana", 15, "normal"), align="center")
    def is_apple_eaten(self,snake,food):
        if (round(snake.the_snake[0].xcor())-20 < food.apple.xcor() and round(snake.the_snake[0].xcor())+20 > food.apple.xcor())  and round(snake.the_snake[0].ycor()) -20 < food.apple.ycor() and round(snake.the_snake[0].ycor()) + 20 > food.apple.ycor()  :
            food.move()
            snake.add_part()
            self.score +=1
            self.score_board.clear()
            self.score_board.goto(0, 250)
            self.score_board.write(f"score :{self.score} ", font=("Verdana", 15, "normal"),align="center")
        else:
            return
    def error_check(self,snake):
        for i in range(1,len(snake.the_snake)-1):
             if snake.the_snake[0].distance(snake.the_snake[i]) < 10 :
                 return True
        if round(snake.the_snake[0].xcor()) > 299 or round(snake.the_snake[0].xcor()) < -299 or round(snake.the_snake[0].ycor()) > 299 or round(snake.the_snake[0].ycor()) < -299 :
                return True
        else:
                return False
