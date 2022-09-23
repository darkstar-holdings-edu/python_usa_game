from turtle import Screen
from game import Board
import pandas as pd  # type: ignore
import re


GAME_TITLE = "Name the US States"
BOARD_IMAGE_FILENAME = "assets/blank_states_img.gif"
GAME_DATA_FILENAME = "data/50_states.csv"
SCREEN_DIMENSION = {"width": 725, "height": 491}
GAME_DATA = pd.read_csv(GAME_DATA_FILENAME)
TOTAL_STATES = len(GAME_DATA)


def main() -> None:
    screen = Screen()
    screen.setup(
        width=SCREEN_DIMENSION["width"],
        height=SCREEN_DIMENSION["height"],
    )
    screen.bgpic(BOARD_IMAGE_FILENAME)
    screen.title(GAME_TITLE)
    screen.tracer(0)

    board = Board(
        width=SCREEN_DIMENSION["width"],
        height=SCREEN_DIMENSION["height"],
    )

    game_running = True
    while game_running:
        guess = screen.textinput(
            title=f"SCORE {board.score}/50", prompt="What is your guess?"
        )

        if guess is None:
            game_running = False
            break

        parsed_guess = re.sub(" +", " ", guess.title().strip())
        if parsed_guess not in board.found_states:
            found_state = GAME_DATA[GAME_DATA.state == parsed_guess]
            if not found_state.empty:
                values = found_state.values[0]
                board.add_state(
                    name=values[0],
                    position=(values[1], values[2]),
                )

        if board.score == TOTAL_STATES:
            game_running = False

        screen.update()

    if board.score == TOTAL_STATES:
        board.show_win_message()
    else:
        board.game_over()

    screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
