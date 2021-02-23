from typing import Any

from pythonk.internal.types.base_type import BaseType


class Boolean(BaseType):

    def get(self) -> Any:
        return bool(self.value)

    pass


class String(BaseType):

    def get(self) -> Any:
        return str(self.value)

    pass


class Number(BaseType):

    def get(self) -> Any:
        return int(self.value)

    pass
