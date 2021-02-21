from rply.token import BaseBox


class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        pass

    pass