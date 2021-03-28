from pythonk.ast.types.data_types import Number, String, Boolean
from pythonk.parser.internal.standard_grammar import StandardGrammar


class DataTypes(StandardGrammar):

    def load_grammar(self):

        @self.parser.production('expression : const')
        def expression_const(p):
            return p[0]

        @self.parser.production('const : BOOLEAN')
        def number(p):
            finalized_bool: str = ""
            given_bool: str = p[0].getstr()

            if given_bool == "false":
                finalized_bool = "False"
            elif given_bool == "true":
                finalized_bool = "True"

            return Boolean(finalized_bool)

        @self.parser.production('const : NUMBER')
        def number(p):
            return Number(int(p[0].getstr()))

        @self.parser.production('const : STRING')
        def string(p):
            return String(p[0].getstr().strip('"\''))

        pass

    pass
