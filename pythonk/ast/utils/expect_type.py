from rply import Token

from pythonk.ast.types.base_type import BaseType
from pythonk.ast.types.data_types import ExAny


class ExpectType:

    @staticmethod
    def check_type(value: Token, expected_type: BaseType):
        got_type = ExpectType.get_exp_type(value)

        if got_type is not expected_type.get_type_name(expected_type):
            raise ArgumentTypeError(f"type {expected_type.get_type_name(expected_type)} cannot be assigned with type {got_type}")
        pass

    @staticmethod
    def get_exp_type(value: Token) -> str:
        if value is not ExAny:
            return value.get_type_name()
        else:
            return "any"

    pass


class ArgumentTypeError(Exception):
    pass
