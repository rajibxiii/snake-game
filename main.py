from turtle import Screen
from snake import Snake
import time

snake = Snake()
screen = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title ("Snake Rax")
screen.tracer(0) # this method accelearates the complex graphics

gameOn = True
while gameOn:
    screen.update() # updates screen every time after the below loop is executed
    time.sleep(1) # waits a second before the next update
    snake.move()

screen.exitonclick()




#TODO: create a snake body
#TODO: move the snake
#TODO: create snake food
#TODO: detect collision with food
#TODO: create a scoreboard
#TODO: detect collision with wall
#TODO: detect collision with tail