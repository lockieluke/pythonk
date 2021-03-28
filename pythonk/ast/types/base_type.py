from typing import Any

from rply.token import BaseBox


class BaseType(BaseBox):

    def __init__(self, value):
        self.value = value
        self.value = self.get_value()
        pass

    def get_value(self) -> any:
        return any(None)

    def get_type_name(self) -> str:
        return "any"

    def eval(self):
        return self.value

    pass
