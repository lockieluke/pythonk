from pythonk.internal.types.data_types import Number, String
from pythonk.parser.internal.standard_grammar import StandardGrammar


class DataTypes(StandardGrammar):

    def load_grammar(self):
        @self.parser.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.parser.production('expression : STRING')
        def string(p):
            return String(p[0].value)
        pass

    pass
