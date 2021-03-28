from pythonk.ast.types.base_type import BaseType


class Boolean(BaseType):

    def get_value(self) -> any:
        return self.value

    def get_type_name(self) -> str:
        return "bool"

    pass


class String(BaseType):

    def get_value(self) -> any:
        return f"\"{str(self.value)}\""

    def get_type_name(self) -> str:
        return "string"

    pass


class Number(BaseType):

    def get_value(self) -> any:
        return int(self.value)

    def get_type_name(self) -> str:
        return "int"

    pass


class ExAny(BaseType):

    def get_value(self) -> any:
        return any(self.value)

    def get_type_name(self) -> str:
        return "any"

    pass
