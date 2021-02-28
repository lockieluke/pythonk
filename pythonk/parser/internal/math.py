
from pythonk.ast.math import Sum, Sub, Times, Divide
from pythonk.ast.utils.expect_type import ExpectType
from pythonk.parser.internal.err_handling import ArithmeticOperationTypeError
from pythonk.parser.internal.standard_grammar import StandardGrammar


class Math(StandardGrammar):

    def load_grammar(self):

        @self.parser.production('expression : expression SUM expression')
        @self.parser.production('expression : expression SUB expression')
        @self.parser.production('expression : expression TIMES expression')
        @self.parser.production('expression : expression DIVIDE expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]

            left_type = ExpectType.get_exp_type(left)
            right_type = ExpectType.get_exp_type(right)

            if left_type == right_type and left_type == "Number":
                if operator.gettokentype() == 'SUM':
                    return Sum(left, right)
                elif operator.gettokentype() == 'SUB':
                    return Sub(left, right)
                elif operator.gettokentype() == 'TIMES':
                    return Times(left, right)
                elif operator.gettokentype() == 'DIVIDE':
                    return Divide(left, right)
                pass
            elif left_type == right_type and left_type == "String":
                if operator.gettokentype() == 'SUM':
                    return Sum(left, right)
                else:
                    raise ArithmeticOperationTypeError(
                        f"{left_type} and {right_type} cannot perform {operator.gettokentype()} Arithmetic Operation")
            elif not left_type == right_type:
                raise ArithmeticOperationTypeError(f"{left_type} and {right_type} cannot perform Arithmetic Operation")

        pass

    pass
