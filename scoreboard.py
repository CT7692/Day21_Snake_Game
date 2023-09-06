from turtle import Turtle
ALIGNMENT = "center"
MY_FONT = ('Verdana', 15, 'normal')
class Scoreboard(Turtle):
    score = 0
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("white")
        self.sety(260)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=MY_FONT)


    def scored(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.sety(0)
        self.write(arg="Game Over", move=False, align=ALIGNMENT, font=MY_FONT)