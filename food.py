from turtle import Turtle
import secrets

MAX = 270
MIN = -270
FOOD_MEASURE = 0.5

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=FOOD_MEASURE, stretch_wid=FOOD_MEASURE)
        self.color("green")
        self.speed("fastest")
        self.new_position()
    def new_position(self):
        self.setpos(x=secrets.SystemRandom().randint(MIN, MAX), y=secrets.SystemRandom().randint(MIN, MAX))
