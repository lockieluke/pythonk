class BaseToken():

    tokens: dict

    def __init__(self, tokens: dict):
        self.tokens = tokens
        pass

    def get_tokens(self) -> dict:
        return self.tokens
        pass

    pass
