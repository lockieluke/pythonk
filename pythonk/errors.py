class pykCompileError(Exception):
    """Base class for all Compiling Errors."""
    def __init__(self, msg=None, ln: int = 0, cn: int = 0):
        self.msg = msg
        self.ln = ln
        self.cn = cn
    name="Compiler Error"
    code=-1
class pykBadArgument(pykCompileError):
    """Argument supply is invalid."""
    name="Bad Argument Given"
    code=-2
class pykInternalCompilerError(pykCompileError):
    """Unknown Fatal Error occurred."""
    name="Internal Compiler Error"
    code=1
class pykSyntaxError(pykCompileError):
    """Syntax Error found in script."""
    name="Syntax Error"
    code=2