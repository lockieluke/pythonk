from rply import LexerGenerator
from rply.lexer import Lexer

from pythonk.lexer.lib_token import lib_token


class PythonkLexer:
    lexer: LexerGenerator
    tokens: dict = lib_token
    ignore_tokens: dict = {
        ""
    }

    def __init__(self):
        self.lexer = LexerGenerator()
        pass

    def add_tokens(self):
        for key in dict.keys(self.tokens):
            self.lexer.add(key, self.tokens[key])
            pass
        self.lexer.ignore(r'[ \t\r\f\v]+')
        pass

    def get_lexer(self) -> Lexer:
        self.add_tokens()
        return self.lexer.build()
        pass

    pass
