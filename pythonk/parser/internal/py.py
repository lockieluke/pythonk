from pythonk.ast.py import PyEvalOperation
from pythonk.ast.types.data_types import String
from pythonk.ast.utils.expect_type import ExpectType
from pythonk.parser.internal.standard_grammar import StandardGrammar


class Py(StandardGrammar):

    def load_grammar(self):
        @self.parser.production("program : PY_EVAL OPEN_PAREN expression CLOSE_PAREN SEMICOLON")
        @self.parser.production("program : NO_COMPILE OPEN_PAREN expression CLOSE_PAREN SEMICOLON")
        def py_eval(p):
            ExpectType.check_type(p[2], String)
            return PyEvalOperation(p[2])
        pass

    pass
