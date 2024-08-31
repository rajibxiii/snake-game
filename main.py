from turtle import Turtle, Screen

snakeHead = Turtle()
snakeBody = Turtle()
snakeTail = Turtle()

snakeHead.shape("square")
snakeBody.shape("square")
snakeTail.shape("square")

snakeHead.color("white")
snakeBody.color("white")
snakeTail.color("white")

snakeBody.goto(-20, 0)
snakeTail.goto(-40, 0)















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