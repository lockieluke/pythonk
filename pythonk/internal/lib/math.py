from pythonk.internal.logic.assignment import BinaryOp


class Sum(BinaryOp):
    def eval(self):
        return f"{self.left.eval()} + {self.right.eval()}"

    pass


class Sub(BinaryOp):
    def eval(self):
        return f"{self.left.eval()} - {self.right.eval()}"

    pass


class Times(BinaryOp):
    def eval(self):
        return f"{self.left.eval()} * {self.right.eval()}"

    pass


class Divide(BinaryOp):
    def eval(self):
        return f"{self.left.eval()} / {self.right.eval()}"

    pass
