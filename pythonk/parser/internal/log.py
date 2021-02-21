from internal.lib.log import LogOperation
from parser.internal.standard_lib import StandardLib


class Log(StandardLib):

    def load_grammar(self):
        @self.parser.production('program : LOG OPEN_PAREN expression CLOSE_PAREN SEMICOLON')
        def program(p):
            return LogOperation(p[2])
        pass

    pass
