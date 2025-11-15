import sys
import os


def good():
    return sys.stdout.isatty()


def size():
    if good():
        x = os.get_terminal_size()
        return x.columns, x.lines
    else:
        return 0, 0
