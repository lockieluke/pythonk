from pythonk.ast.internal_operation import InternalOperation

from pythonk.ast.utils.str import StrUtils
from pythonk.parser.internal.err_handling import ArgumentTypeError


class PyEvalOperation(InternalOperation):

    def run(self):
        return self.value.value[1:-1]

    pass
