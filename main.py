from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title ("Snake Rax")
screen.tracer(0) # this method accelearates the complex graphics

# asking for speed setting
snakeSpeed = 0
while snakeSpeed <= 0 or snakeSpeed >10:
    snakeSpeed = int(screen.textinput(title="Set Snake Speed", prompt="What speed do you want for your snake? (from 1 to 10)"))

snake = Snake()
snake.makeSnake()
food = Food()
scores = Scoreboard(snakeSpeed)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameOn = True
snakeSleep = 1.1-(snakeSpeed/10) # if speed is 10, sleep is 0.1. if 6, then 0.5
while gameOn:
    screen.update() # updates screen every time after the below loop is executed
    time.sleep(snakeSleep) # waits a second before the next update
    snake.move()

    if snake.head.distance(food) < 15: # when snake hits the food
        food.refresh()
        snake.extend()
        scores.addScore()

    # when snake collides to the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameOn = False
        scores.gameOver()
    
    # when snake collides to any other part of the body
    for i in snake.snakeSegments[1:]: # slicing the list
        # skipped first item, because the distance between head and head is 0, that is less than 10
        if snake.head.distance(i) < 10: # if the distance between head and any other segment is less than 10
            gameOn = False
            scores.gameOver()

screen.exitonclick()