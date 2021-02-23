from pythonk.compiler.config import CompilerConfig
from pythonk.internal.lib.internal_operation import InternalOperation


class BasicOperation(InternalOperation):

    def run(self):
        if not CompilerConfig.get_remove_comments():
            return f"# {self.value.eval()}"
        else:
            return ''

    pass
