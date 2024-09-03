from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.initialPosition = [(20, 0), (0, 0), (-20, 0)]
        self.snakeSegments = []
    
    def makeSnake (self):
        for i in self.initialPosition: # creating three segments of a snake
            self.add_segments(i) # i is the position where the segment will be added
        self.head = self.snakeSegments[0]
    
    def add_segments (self, position):
        snakeSegment = Turtle()
        snakeSegment.shape ("square")
        snakeSegment.color("white")
        snakeSegment.penup()
        snakeSegment.goto(position)
        self.snakeSegments.append(snakeSegment)

    def extend (self):
        position = self.snakeSegments[-1].position() # negative value starts the loop from the last # position is a method of turtle class
        self.add_segments(position)

    def move (self):
        for segment_number in range (len(self.snakeSegments)-1, 0, -1): # just a reverse loop (from 2 to 1, 0 is excluded)
            new_x = self.snakeSegments [segment_number-1].xcor() # getting the x coordinate of second last segment
            new_y = self.snakeSegments [segment_number-1].ycor() # getting the y coordinate of second last segment
            self.snakeSegments[segment_number].goto(new_x, new_y) # going to the poisition of the second last segment from the last segment
            # all the segments are moved, except the first one
        self.head.forward(20) # now forwarding the first segment

    def up (self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right (self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left (self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def down (self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

