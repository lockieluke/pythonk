from rply import Token

from pythonk.ast.types.base_type import BaseType


class ExpectType:

    @staticmethod
    def check_type(value: Token, expected_type: BaseType):
        got_type = type(value).__name__
        expected_type = expected_type.__name__

        if got_type is not expected_type:
            raise ArgumentTypeError(f"{expected_type} cannot be assigned with type {got_type}")
        pass

    pass


class ArgumentTypeError(Exception):
    pass
