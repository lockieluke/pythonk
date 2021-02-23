
from pythonk.internal.lib.math import Sum, Sub, Times, Divide
from pythonk.internal.utils.int import IntUtils
from pythonk.internal.utils.str import StrUtils
from pythonk.parser.internal.err_handling import ArithmeticOperationTypeError
from pythonk.parser.internal.standard_lib import StandardGrammar


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

            if not IntUtils.which_not(left.eval(), right.eval()) == 'none' and not StrUtils.which_not(left.eval(), right.eval()) == 'none':
                raise ArithmeticOperationTypeError("Arithmetic Operation is only allowed if both sides are number")
            elif StrUtils.which_not(left.eval(), right.eval()) == 'none':
                if operator.gettokentype() == 'SUM':
                    return Sum(left, right)
                pass

            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'TIMES':
                return Times(left, right)
            elif operator.gettokentype() == 'DIVIDE':
                return Divide(left, right)

        pass

    pass
