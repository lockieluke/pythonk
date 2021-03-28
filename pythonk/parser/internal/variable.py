from pythonk.ast.utils.expect_type import ExpectType
from pythonk.ast.variable import VariableAssignmentOperation, VariableGetterOperation, VariableSetterOperation
from pythonk.parser.internal.standard_grammar import StandardGrammar


class Variable(StandardGrammar):

    def load_grammar(self):
        @self.parser.production("program : VAR_CLET VAR_IDENTIFIER = expression SEMICOLON")
        @self.parser.production("program : VAR_LET VAR_IDENTIFIER = expression SEMICOLON")
        def var_define(p):
            return VariableAssignmentOperation(p[1], p[3], p[0].name == "VAR_CLET")

        @self.parser.production("expression : VAR_IDENTIFIER")
        def var_read(p):
            return VariableGetterOperation(p[0])

        @self.parser.production("program : VAR_IDENTIFIER = expression SEMICOLON")
        def var_set(p):
            return VariableSetterOperation(p[0], p[2])

        @self.parser.production("program : VAR_CLET VAR_IDENTIFIER COLON expression = expression SEMICOLON")
        @self.parser.production("program : VAR_LET VAR_IDENTIFIER COLON expression = expression SEMICOLON")
        def typed_var_define(p):
            return VariableAssignmentOperation(p[1], p[5], p[0].name == "VAR_CLET", p[3].value.value)

    pass
