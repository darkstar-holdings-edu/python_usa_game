from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"


class WinMessage(Turtle):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__()

        self.color("black")
        self.penup()
        self.hideturtle()
        self.setposition(position)
        self.write("You Win!", False, align=ALIGNMENT, font=FONT)
