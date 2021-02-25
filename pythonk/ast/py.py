from pythonk.ast.internal_operation import InternalOperation


class PyEvalOperation(InternalOperation):

    def run(self):
        return self.value.value[1:-1]

    pass
