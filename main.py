from turtle import Turtle, Screen
import time

screen = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title ("Snake Rax")
screen.tracer(0) # this method accelearates the complex graphics

initialPosition = [(-20, 0), (0, 0), (20, 0)]
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
    for segment in snakeSegments:
        segment.forward(20)
        




screen.exitonclick()




#TODO: create a snake body
#TODO: move the snake
#TODO: create snake food
#TODO: detect collision with food
#TODO: create a scoreboard
#TODO: detect collision with wall
#TODO: detect collision with tail