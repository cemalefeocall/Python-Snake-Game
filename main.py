from turtle import Screen
from time import sleep
from SnakeClass import Snake
from FoodClass import Food
from ScoreboardClass import Scoreboard

screen = Screen()

# setuping the screen 600x600
screen.setup(width=600,height=600)

# changing the background colour
screen.bgcolor("black")

# setting up the title
screen.title(titlestring="Snake Game")

#closing the tracer function
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard =Scoreboard()

screen.listen()

screen.onkey(fun=snake.turn_up,key="w")
screen.onkey(fun=snake.turn_down,key="s")
screen.onkey(fun=snake.turn_left,key="a")
screen.onkey(fun=snake.turn_right,key="d")

scoreboard.initScoreboard()


while True:
    screen.update()
    sleep(0.1)
    if food.detectCollisionWithFood(snake.snake_head.pos()):
        food.increaseScoreValue()
        snake.addSnakeSegments()
        scoreboard.updateScoreboard(food.getScoreValue())
    snake.WallColision()
    if snake.checkTailCollision():
        scoreboard.loseScreen(food.getScoreValue())
        break
    snake.move()

screen.exitonclick()








