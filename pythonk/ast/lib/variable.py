from rply.token import BaseBox, Token

from pythonk.compiler.compile_stream import CompileStream

let_var_env: dict = {}
const_var_env: dict = {}


def check_var_defined(var_name: str) -> bool:
    if var_name in let_var_env.values() or var_name in const_var_env.values():
        return True
    else:
        return False

    pass


def check_clet_or_let(var_name: str) -> str:
    if var_name in let_var_env.values():
        return 'let'
    elif var_name in const_var_env.values():
        return 'clet'

    pass


class VariableSetterOperation(BaseBox):

    def __init__(self, var_name: Token, var_expression: Token):
        self.var_name = var_name
        self.var_expression = var_expression
        pass

    def eval(self):
        if check_var_defined(self.var_name.value):
            if check_clet_or_let(self.var_name.value) == 'let':
                CompileStream.add_stream(f"{self.var_name.value} = {self.var_expression.value}")
            else:
                raise AssignmentError("Constant(clet) variable cannot be reassigned")
        else:
            raise VariableError(f"Variable {self.var_name.value} was not defined")

    pass


class VariableAssignmentOperation(BaseBox):

    def __init__(self, var_name: Token, var_expression: Token, const: bool = False):
        self.var_name = var_name
        self.var_expression = var_expression
        self.const = const
        pass

    def eval(self):
        var_name: str = self.var_name.value
        var_expression: str = self.var_expression.value

        # Variable was assigned to something and was found in vmm(variable memory map)
        if check_var_defined(var_name):
            raise AssignmentError(f"Variable {var_name} cannot be reassign")

        # Put variable into vmm so that we can find out if the variable was assigned later
        if not self.const:
            let_var_env[CompileStream.get_compiling_file()] = var_name
        else:
            const_var_env[CompileStream.get_compiling_file()] = var_name
        CompileStream.add_stream(f"{var_name} = {var_expression}")
        pass

    pass


class VariableGetterOperation(BaseBox):

    def __init__(self, value):
        self.value = value
        pass

    def eval(self):
        if check_var_defined(self.value.value):
            return self.value.value
        else:
            raise VariableError(f"Variable {self.value.value} was not defined")

    pass


class AssignmentError(Exception):
    pass


class VariableError(Exception):
    pass
