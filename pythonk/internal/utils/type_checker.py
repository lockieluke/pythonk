import re


class TypeChecker:

    regex: str = ""

    @classmethod
    def init_type_checker(cls, regex):
        cls.regex = regex
        pass


    @classmethod
    def is_valid(cls, value) -> bool:
        if not re.compile(cls.regex).match(value):
            return False
        else:
            return True
        pass

    @classmethod
    def which_not(cls, left, right) -> str:
        left = str(left)
        right = str(right)
        if cls.is_valid(left) and cls.is_valid(right):
            return 'none'
        elif cls.is_valid(left) and not cls.is_valid(right):
            return 'right'
        elif not cls.is_valid(left) and cls.is_valid(right):
            return 'left'
        else:
            return 'none'
        pass

    pass
