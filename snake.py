from turtle import Turtle

starting_position=[(0,0),(-20,0),(-40,0)]
move_distance=20

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()


    def create_snake(self):
        for position in starting_position:
            segment=Turtle("square")
            segment.color("white")
            segment.penup()

            segment.goto(position)


            self.segments.append(segment)

    def add_new_segment(self):
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(self.segments[len(self.segments)-1].xcor(),self.segments[len(self.segments)-1].ycor())
            self.segments.append(new_segment)



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()