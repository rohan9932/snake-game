from turtle import Turtle
COLOR = "black"
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        '''Creates the snake'''
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        '''Adds a segment'''
        segment = Turtle("square")
        segment.color(COLOR)
        segment.up()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        '''Extends the snake body'''
        self.add_segment(self.segments[-1].position())

    def move(self):
        '''Moves the snake automatically'''
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        '''Moves up'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''Moves down'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        '''Moves left'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''Moves right'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        '''Resets the snake'''
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
