from pythonk.ast.lib.basic import BasicOperation
from pythonk.parser.internal.standard_grammar import StandardGrammar


class Basic(StandardGrammar):

    def load_grammar(self):
        @self.parser.production('program : COMMENT expression')
        def comment(p):
            return BasicOperation(p[1])
        pass

    pass
