from pythonk.parser.internal.standard_lib import StandardGrammar


class ErrorHandling(StandardGrammar):

    def load_grammar(self):
        @self.parser.error
        def error_handle(token):
            raise ValueError(token)

        pass

    pass


class ArithmeticOperationTypeError(Exception):
    pass

class ArgumentTypeError(Exception):
    pass
