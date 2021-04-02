from pythonk.internal.lib.internal_operation import InternalOperation

from pythonk.internal.utils.str import StrUtils
from pythonk.parser.internal.err_handling import ArgumentTypeError


class PyEvalOperation(InternalOperation):

    def run(self):
        if StrUtils.is_valid(str(self.value.eval())):
            return self.value.eval()[1:-1]
        else:
            raise ArgumentTypeError("Function argument does not accept type other than 'string'")

    pass
