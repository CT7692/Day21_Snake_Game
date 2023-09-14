from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

BOUNDARY1 = 290
BOUNDARY2 = -290
SCREEN_MEASURE = 600
TOO_CLOSE = 15

def play(my_snake, screen_obj):
    game_on = True
    snake_food = Food()
    score = Scoreboard()
    while game_on:
        screen_obj.update()
        sleep(0.1)
        my_snake.move()
        gameplay(my_snake, screen_obj, snake_food, score)
        for i in my_snake.body[1:]:
            if my_snake.body[0].distance(i) < TOO_CLOSE:
                game_on = False
                score.game_over()
        if (my_snake.body[0].xcor() > BOUNDARY1 or my_snake.body[0].xcor() < BOUNDARY2 or
                my_snake.body[0].ycor() > BOUNDARY1 or my_snake.body[0].ycor() < BOUNDARY2):
            game_on = False
            score.game_over()
    return game_on

def gameplay(my_snake, screen_obj, my_food, my_score):
    screen_obj.listen()
    screen_obj.onkey(key="Up", fun=my_snake.up)
    screen_obj.onkey(key="Down", fun=my_snake.down)
    screen_obj.onkey(key="Left", fun=my_snake.left)
    screen_obj.onkey(key="Right", fun=my_snake.right)
    when_snake_eats(my_snake, my_food, my_score)

def when_snake_eats(my_snake, my_food, my_score):
    if my_snake.body[0].distance(my_food) <  TOO_CLOSE:
        my_snake.food_eaten()
        my_food.new_position()
        my_score.scored()


my_screen = Screen()
my_screen.setup(width=SCREEN_MEASURE, height=SCREEN_MEASURE)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)
serpent = Snake()
active = play(serpent, my_screen)
my_screen.update
my_screen.exitonclick()
