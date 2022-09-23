from turtle import Turtle, pos

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"


class GameOver(Turtle):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__()

        self.color("black")
        self.penup()
        self.hideturtle()
        self.setposition(position)
        self.write("Game Over!", False, align=ALIGNMENT, font=FONT)
