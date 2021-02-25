from pythonk.ast.types.data_types import Number, String, Boolean
from pythonk.parser.internal.standard_grammar import StandardGrammar


class DataTypes(StandardGrammar):

    def load_grammar(self):

        @self.parser.production('expression : const')
        def expression_const(p):
            return p[0]

        @self.parser.production('const : BOOLEAN')
        def number(p):
            return Boolean(p[0].getstr())

        @self.parser.production('const : NUMBER')
        def number(p):
            return Number(int(p[0].getstr()))

        @self.parser.production('const : STRING')
        def string(p):
            return String(p[0].getstr().strip('"\''))

        pass

    pass
