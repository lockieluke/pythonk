from pythonk.lexer.token.base_token import BaseToken

VariableToken: BaseToken = BaseToken({
    "VAR_LET": r"let(?!\w)",
    "VAR_CLET": r"clet(?!\w)",
    "VAR_IDENTIFIER": r"[a-zA-Z_][a-zA-Z0-9_]*"
})
