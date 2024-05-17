from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
peter_the_snake=Snake()
food_snake=Food()


screen.listen()
screen.onkey(fun=peter_the_snake.up,key="Up")
screen.onkey(fun=peter_the_snake.down,key="Down")
screen.onkey(fun=peter_the_snake.left,key="Left")
screen.onkey(fun=peter_the_snake.right,key="Right")





game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    peter_the_snake.move()

    if peter_the_snake.segments[0].distance(food_snake)<15:
        food_snake.refresh_food()







screen.exitonclick()