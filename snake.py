from turtle import Turtle, Screen
s = Screen()

class Snake:
    def __init__(self):
        self.initialPosition = [(20, 0), (0, 0), (-20, 0)]
        self.snakeSegments = []
    
    def makeSnake (self):
        for i in self.initialPosition: # creating three segments of a snake
            snakeSegment = Turtle()
            snakeSegment.shape ("square")
            snakeSegment.color("white")
            snakeSegment.penup()
            snakeSegment.goto(i)
            self.snakeSegments.append(snakeSegment)
    
    def move (self):
        for segment_number in range (len(self.snakeSegments)-1, 0, -1): # just a reverse loop (from 2 to 1, 0 is excluded)
            new_x = self.snakeSegments [segment_number-1].xcor() # getting the x coordinate of second last segment
            new_y = self.snakeSegments [segment_number-1].ycor() # getting the y coordinate of second last segment
            self.snakeSegments[segment_number].goto(new_x, new_y) # going to the poisition of the second last segment from the last segment
            # all the segments are moved, except the first one
        self.snakeSegments[0].forward(20) # now forwarding the first segment

    def up (self):
        self.snakeSegments[0].setheading(90)

    def right (self):
        self.snakeSegments[0].setheading(0)

    def left (self):
        self.snakeSegments[0].setheading(180)
    
    def down (self):
        self.snakeSegments[0].setheading(270)

