from typing import List

from lexer.token.base_token import BaseToken
from lexer.token.basic import BasicToken
from lexer.token.data_types import DataTypesToken
from lexer.token.log import LogToken
from lexer.token.math import MathToken


def add_token_libs(token_libs: List[BaseToken]) -> dict:
    token_libs_result: dict = {}
    for token_lib in token_libs:
        token_libs_result = token_libs_result | token_lib.get_tokens()
        pass
    return token_libs_result


lib_token = add_token_libs([BasicToken, DataTypesToken, LogToken, MathToken])
