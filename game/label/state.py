from turtle import Turtle

FONT = ("Arial", 10, "normal")


class State(Turtle):
    def __init__(self, text: str, position: tuple[int, int]) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.setposition(position[0], position[1])
        self.write(text, True, font=FONT)
