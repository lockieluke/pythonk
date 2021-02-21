from typing import Any

from rply.token import BaseBox

from compiler.compile_stream import CompileStream


class InternalOperation(BaseBox):

    def __init__(self, value):
        self.value = value
        pass

    def eval(self):
        CompileStream.add_stream(self.run())
        pass

    def run(self) -> Any:
        pass

    pass
