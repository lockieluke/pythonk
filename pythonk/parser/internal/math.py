from pythonk.internal.lib.math import Sum, Sub, Times, Divide
from pythonk.parser.internal.standard_lib import StandardLib


class Math(StandardLib):

    def load_grammar(self):

        @self.parser.production('expression : expression SUM expression')
        @self.parser.production('expression : expression SUB expression')
        @self.parser.production('expression : expression TIMES expression')
        @self.parser.production('expression : expression DIVIDE expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
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
