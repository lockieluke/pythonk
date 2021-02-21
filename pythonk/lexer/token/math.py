from lexer.token.base_token import BaseToken

MathToken: BaseToken = BaseToken({
    "SUM": r"\+",
    "SUB": r"\-",
    "TIMES": r"\*",
    "DIVIDE": r"\/"
})
