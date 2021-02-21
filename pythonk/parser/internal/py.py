from pythonk.internal.lib.py import PyEvalOperation
from pythonk.parser.internal.standard_lib import StandardLib


class Py(StandardLib):

    def load_grammar(self):
        @self.parser.production("program : PY_EVAL OPEN_PAREN expression CLOSE_PAREN SEMICOLON")
        def py_eval(p):
            return PyEvalOperation(p[2])
        pass

    pass
