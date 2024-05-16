from turtle import Turtle,Screen
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

segments=[]
starting_position=[(0,0),(-20,0),(-40,0)]

for position in starting_position:
    segment=Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)





screen.exitonclick()