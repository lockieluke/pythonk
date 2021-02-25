from pythonk.lexer.token.base_token import BaseToken

DataTypesToken: BaseToken = BaseToken({
    "NUMBER": r"\d+",
    "STRING": r'(["])(?:(?=(\\?))\2.)*?\1',
    "BOOLEAN": r"true(?!\w)|false(?!\w)"
})
