from pythonk.internal.lib.log import LogOperation
from pythonk.parser.internal.standard_lib import StandardGrammar


class Log(StandardGrammar):

    def load_grammar(self):
        @self.parser.production('program : LOG OPEN_PAREN expression CLOSE_PAREN SEMICOLON')
        def program(p):
            return LogOperation(p[2])
        pass

    pass
