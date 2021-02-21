from parser.internal.standard_lib import StandardLib


class ErrorHandling(StandardLib):

    def load_grammar(self):
        @self.parser.error
        def error_handle(token):
            raise ValueError(token)

        pass

    pass


class ArithmeticOperationTypeError(Exception):
    pass
