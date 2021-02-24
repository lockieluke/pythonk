import re

from pythonk.ast.utils.type_checker import TypeChecker


class StrUtils(TypeChecker):
    pass


StrUtils.init_type_checker(r'"([^"]*)"')
