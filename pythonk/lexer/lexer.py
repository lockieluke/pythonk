from rply import LexerGenerator
from rply.lexer import Lexer

from lexer.lib_token import lib_token


class PythonkLexer:
    lexer: LexerGenerator
    tokens: dict = lib_token

    def __init__(self):
        self.lexer = LexerGenerator()
        pass

    def _add_tokens(self):
        for key in dict.keys(self.tokens):
            self.lexer.add(key, self.tokens[key])
            pass
        self.lexer.ignore(r'\s+')
        pass

    def get_lexer(self) -> Lexer:
        self._add_tokens()
        return self.lexer.build()
        pass

    pass
