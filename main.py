from turtle import Turtle, Screen

initialPosition = [(-20, 0), (0, 0), (20, 0)]

for i in initialPosition:
    snakeSegment = Turtle()
    snakeSegment.shape ("square")
    snakeSegment.color("white")
    snakeSegment.goto(i)

screen = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title ("Snake Rax")
screen.exitonclick()







#TODO: create a snake body
#TODO: move the snake
#TODO: create snake food
#TODO: detect collision with food
#TODO: create a scoreboard
#TODO: detect collision with wall
#TODO: detect collision with tail