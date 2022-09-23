from turtle import pos
from .label import State, GameOver, WinMessage


class Board:
    found_states: list[str] = []
    score: int = 0
    width: int
    height: int

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def add_state(self, name: str, position: tuple[int, int]) -> None:
        """Adds a piece to the board"""
        self.found_states.append(name)
        State(text=name, position=position)
        self.score += 1

    def game_over(self) -> None:
        """Displays the game over message on the board"""
        GameOver(position=(0, 0))

    def show_win_message(self) -> None:
        """Displays the winner message on the board"""
        WinMessage(position=(0, 0))
