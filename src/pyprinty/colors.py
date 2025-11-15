class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __call__(self, background=False):
        return f"\033[{48 if background else 38};2;{self.red};{self.green};{self.blue}m"


WHITE = Color(255, 255, 255)
MAGENTA = Color(255, 0, 255)
YELLOW = Color(255, 255, 0)
ORANGE = Color(242, 135, 5)
GRAY = Color(128, 128, 128)
CYAN = Color(0, 255, 255)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
RED = Color(255, 0, 0)
BLACK = Color(0, 0, 0)

Initialize_background_color = "\033[49m"
Initialize_text_color = "\033[39m"
Initialize_colors = "\033[39;49m"
