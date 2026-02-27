from functools import partial
from typing import Callable

from ._page import Page, page_func


class Terminal:
    def __init__(self):
        self.last_page = None

    def _page(self, func: Callable, page: Page, /, *args, **kwargs):
        page.start(self.last_page)
        self.last_page = page
        func(*args, **kwargs)
        page.end()

    def page(self, name: str, start: page_func = None, back: page_func = None, end: page_func = None):
        return lambda func: partial(self._page, func, Page(name, start, back, end))
