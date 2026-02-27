from typing import Callable


page_func = Callable[[str], None]
_default_func = lambda name: print(f"=={name}==")


class Page:
    def __init__(self, name: str, start: page_func, back: page_func, end: page_func):
        self._start = start or _default_func
        self._back = back or _default_func
        self._end = end or _default_func
        self._parent = None
        self.name = name

    def start(self, parent):
        self._parent = parent
        self._start(self.name)

    def end(self):
        self._end(self.name)
        if self._parent:
            self._parent.back()

    def back(self):
        self._back(self.name)
