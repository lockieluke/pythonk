from rply import ParserGenerator

from pythonk.parser.global_parser import GlobalParser


class StandardLib:

    parser: ParserGenerator

    def __init__(self):
        self.parser = GlobalParser.get_parser()
        self.load_grammar()
        pass

    def load_grammar(self):
        pass

    pass
