from typing import Any

from rply.token import BaseBox

from pythonk.ast.types.base_type import BaseType


class Boolean(BaseType):

    def get_value(self) -> any:
        return bool(self.value)

    pass


class String(BaseType):

    def get_value(self) -> any:
        return f"\"{str(self.value)}\""

    pass


class Number(BaseType):

    def get_value(self) -> any:
        return int(self.value)

    pass
