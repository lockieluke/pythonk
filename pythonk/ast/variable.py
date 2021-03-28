from rply.token import BaseBox, Token

from pythonk.ast.types.data_types import String
from pythonk.ast.utils.expect_type import ExpectType
from pythonk.compiler.compile_stream import CompileStream

let_var_env: list[dict] = []
const_var_env: list[dict] = []


def save_var(const: bool, var_type: str, var_name: str, filename: str = CompileStream.get_compiling_file()):
    var_object: dict = {
        "name": var_name,
        "type": var_type,
        "filename": filename
    }

    if const:
        const_var_env.append(var_object)
    else:
        let_var_env.append(var_object)

    pass


def check_var_defined(var_name: str) -> bool:
    for var in let_var_env + const_var_env:
        if var["filename"] == CompileStream.get_compiling_file() and var["name"] == var_name:
            return True

    return False


def check_clet_or_let(var_name: str) -> str:
    for var in let_var_env:
        if var["filename"] == CompileStream.get_compiling_file() and var["name"] == var_name:
            return 'let'
        pass

    for var in const_var_env:
        if var["filename"] == CompileStream.get_compiling_file() and var["name"] == var_name:
            return 'clet'
        pass

    raise VariableError(f"Variable {var_name} was not defined")

def get_var_type(var_name: str) -> str:
    for var in let_var_env:
        if var["filename"] == CompileStream.get_compiling_file() and var["name"] == var_name:
            return var["type"]

    raise VariableError(f"Variable {var_name} was not defined")


class VariableSetterOperation(BaseBox):

    def __init__(self, var_name: Token, var_expression: Token):
        self.var_name = var_name
        self.var_expression = var_expression
        pass

    def eval(self):
        if check_var_defined(self.var_name.value):
            if check_clet_or_let(self.var_name.value) == 'let':
                type_name: str = get_var_type(self.var_name.value)
                if not type_name == self.var_expression.get_type_name() and not type_name == "any":
                    raise TypeError(f"{self.var_expression.get_type_name()} should not be assigned to {type_name}")
                CompileStream.add_stream(f"{self.var_name.value} = {self.var_expression.value}")
            else:
                raise AssignmentError("Constant(clet) variable cannot be reassigned")
        else:
            raise VariableError(f"Variable {self.var_name.value} was not defined")

    pass


class VariableAssignmentOperation(BaseBox):

    native_type_remap: dict = {
        "any": "any",
        "string": "str",
        "int": "int",
        "bool": "bool"
    }

    def __init__(self, var_name: Token, var_expression: Token, const: bool = False, var_type: str = 'any'):
        self.var_name = var_name
        self.var_expression = var_expression
        self.const = const
        self.var_type = var_type
        pass

    def eval(self):
        var_name: str = self.var_name.value
        var_expression: str = self.var_expression.value
        var_type: str = self.var_type

        # Variable was assigned to something and was found in vmm(variable memory map)
        if check_var_defined(var_name):
            raise AssignmentError(f"Variable {var_name} cannot be reassigned")

        # Check if the given type annotation is in type remap
        if var_type not in self.native_type_remap.keys():
            raise TypeError(f"Type {var_type} is an unknown type")

        if not var_type == self.var_expression.get_type_name() and not var_type == "any":
            raise TypeError(f"{ExpectType.get_exp_type(self.var_expression)} should not be assigned to {var_type}")

        # Put variable into vmm so that we can find out if the variable was assigned later
        save_var(self.const, self.var_type, self.var_name.value)
        CompileStream.add_stream(f"{var_name}: {self.native_type_remap[var_type]} = {var_expression}")
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
