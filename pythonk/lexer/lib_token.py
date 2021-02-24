from typing import List

from pythonk.lexer.token.base_token import BaseToken
from pythonk.lexer.token.basic import BasicToken
from pythonk.lexer.token.data_types import DataTypesToken
from pythonk.lexer.token.log import LogToken
from pythonk.lexer.token.math import MathToken
from pythonk.lexer.token.py import PyToken
from pythonk.lexer.token.variable import VariableToken


def add_token_libs(token_libs: List[BaseToken]) -> dict:
    token_libs_result: dict = {}
    for token_lib in token_libs:
        token_libs_result = token_libs_result | token_lib.get_tokens()
        pass
    return token_libs_result


lib_token = add_token_libs([BasicToken, DataTypesToken, LogToken, MathToken, PyToken, VariableToken])
