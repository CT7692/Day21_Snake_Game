from turtle import Turtle

SPEED = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
class Snake:
    body = []
    x_pos = 20
    y_pos = 0
    def __init__(self):
        for i in range(0, 3):
            new_piece = Turtle(shape="square")
            new_piece.color("white")
            new_piece.up()
            self.x_pos -= 20
            new_piece.setx(self.x_pos)
            self.body.append(new_piece)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.body[0].forward(SPEED)

    def up(self):
        if self.body[0].heading() != DOWN:
            self.body[0].seth(UP)

    def down(self):
        if self.body[0].heading() != UP:
            self.body[0].seth(DOWN)

    def left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].seth(LEFT)

    def right(self):
        if self.body[0].heading() != LEFT:
            self.body[0].seth(RIGHT)

    def food_eaten(self):
        new_piece = Turtle(shape="square")
        new_piece.speed("fastest")
        new_piece.color("white")
        new_piece.up()
        new_piece.goto(self.body[-1].position())
        self.body.append(new_piece)
