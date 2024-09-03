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

snake = Snake()
snake.makeSnake()
food = Food()
scores = Scoreboard(2) #TODO: prompt for speed

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameOn = True
while gameOn:
    screen.update() # updates screen every time after the below loop is executed
    time.sleep(0.3) # waits a second before the next update
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
    for i in snake.snakeSegments:
        if i == snake.head: # off course, distance between head and head is 0, that is less than 10
            pass
        elif snake.head.distance(i) < 10: # if the distance between head and any other segment is less than 10
            gameOn = False
            scores.gameOver()

screen.exitonclick()




#TODO: create a snake body
#TODO: move the snake
#TODO: create snake food
#TODO: detect collision with food
#TODO: create a scoreboard
#TODO: detect collision with wall
#TODO: detect collision with tail