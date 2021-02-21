from pythonk.internal.lib.internal_operation import InternalOperation


class LogOperation(InternalOperation):

    def run(self):
        return f"print({self.value.eval()})"

    pass
