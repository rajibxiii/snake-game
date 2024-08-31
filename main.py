from turtle import Turtle, Screen
import time

screen = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title ("Snake Rax")
screen.tracer(0) # this method accelearates the complex graphics

initialPosition = [(20, 0), (0, 0), (-20, 0)] # seg1 seg2 seg3 (from right of the snake)
snakeSegments = []

for i in initialPosition: # creating three segments of a snake
    snakeSegment = Turtle()
    snakeSegment.shape ("square")
    snakeSegment.color("white")
    snakeSegment.penup()
    snakeSegment.goto(i)
    snakeSegments.append(snakeSegment)

gameOn = True
while gameOn:
    time.sleep(1) # waits a second before the next update
    screen.update() # updates screen every time after the below loop is executed

    for segment_number in range (len(snakeSegments)-1, 0, -1): # just a reverse loop
        new_x = snakeSegments [segment_number-1].xcor() # getting the x coordinate of second last segment
        new_y = snakeSegments [segment_number-1].ycor() # getting the y coordinate of second last segment
        snakeSegments[segment_number].goto(new_x, new_y) # going to the poisition of the second last segment from the last segment
        # all the segments are moved
    snakeSegments[0].forward(20) # now forwarding the first segment
    snakeSegments[0].left(90)

screen.exitonclick()




#TODO: create a snake body
#TODO: move the snake
#TODO: create snake food
#TODO: detect collision with food
#TODO: create a scoreboard
#TODO: detect collision with wall
#TODO: detect collision with tail