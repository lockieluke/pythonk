from rply import ParserGenerator

from lexer.lexer import PythonkLexer

parser: ParserGenerator = None

class GlobalParser:

    @staticmethod
    def init_parser():
        global parser
        parser = ParserGenerator(dict.keys(PythonkLexer.tokens))
        pass

    @staticmethod
    def get_parser() -> ParserGenerator:
        global parser
        return parser

    @staticmethod
    def set_parser(parser_gen: ParserGenerator):
        global parser
        parser = parser_gen
        pass

    pass
