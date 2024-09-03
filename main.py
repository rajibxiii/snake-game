from turtle import Screen
from snake import Snake
import time

screen = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title ("Snake Rax")
screen.tracer(0) # this method accelearates the complex graphics

snake = Snake()
snake.makeSnake()

# screen.listen()
# screen.onkey(snake.up, "Up")


gameOn = True
while gameOn:
    screen.update() # updates screen every time after the below loop is executed
    time.sleep(0.1) # waits a second before the next update
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    snake.move()

screen.exitonclick()




#TODO: create a snake body
#TODO: move the snake
#TODO: create snake food
#TODO: detect collision with food
#TODO: create a scoreboard
#TODO: detect collision with wall
#TODO: detect collision with tail