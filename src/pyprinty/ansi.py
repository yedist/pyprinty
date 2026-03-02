class Ansi:
    custom_background_color = lambda r, g, b: f"\033[48;2;{r};{g};{b}m"
    custom_text_color = lambda r, g, b: f"\033[38;2;{r};{g};{b}m"
    bold = "\033[1m"
