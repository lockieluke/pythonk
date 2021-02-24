from pythonk.lexer.token.base_token import BaseToken

BasicToken: BaseToken = BaseToken({
    "OPEN_PAREN": r"\(",
    "CLOSE_PAREN": r"\)",
    "SEMICOLON": r"\;",
    "COLON": r"\:",
    "SPACE": r"\s",
    "COMMENT": r"\#\s",
    "=": r"\="
})
