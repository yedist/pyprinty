class Ansi:
    CUSTOM_BACKGROUND_COLOR = lambda r, g, b: f"\033[48;2;{r};{g};{b}m"
    CUSTOM_TEXT_COLOR = lambda r, g, b: f"\033[38;2;{r};{g};{b}m"

    BOLD = "\033[1m"
    NO_BOLD = "\033[22m"
    RESET_TEXT_EFFECTS = NO_BOLD

    CLEAR_CURSOR_RIGHT = "\033[0K"
    CLEAR_CURSOR_LEFT = "\033[1K"
    CLEAR_CURSOR_DOWN = "\033[0J"
    CLEAR_CURSOR_UP = "\033[1J"
    CLEAR_TERMINAL = "\033c"
    CLEAR_SCREEN = "\033[2J"
    CLEAR_LINE = "\033[2K"

    RESET_TEXT_COLOR = "\033[39m"
    RESET_BACKGROUND = "\033[49m"
    RESET_STYLE = "\033[0m"

    CURSOR_MOVE = lambda row, col: f"\033[{row};{col}H"
    CURSOR_UP = lambda n=1: f"\033[{n}A"
    CURSOR_DOWN = lambda n=1: f"\033[{n}B"
    CURSOR_RIGHT = lambda n=1: f"\033[{n}C"
    CURSOR_LEFT = lambda n=1: f"\033[{n}D"
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"
