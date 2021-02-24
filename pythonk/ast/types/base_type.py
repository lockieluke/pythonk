from typing import Any

from rply.token import BaseBox


class BaseType(BaseBox):

    def __init__(self, value):
        self.value = value
        pass

    def eval(self):
        return self.get()

    def get(self) -> Any:
        pass

    pass
