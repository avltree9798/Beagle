from utils.constants import (
    TOKEN_DICTIONARY,
    EXPRESSION,
    NUMBER,
    VARIABLE_ASSIGNMENT,
    functions
)

RESERVED_KEYWORDS = set(functions.keys())
class BeagleToken:

    def __init__(self, type, value, name=None): 
        self.type = type
        assert self.type in TOKEN_DICTIONARY.keys()
        self.value = value
        self.name = name

    def __repr__(self):
        if self.type != VARIABLE_ASSIGNMENT:
            return f'<BeagleToken({TOKEN_DICTIONARY.get(self.type)}, "{self.value}" at {id(self)})>'
        else:
            return f'<BeagleToken({TOKEN_DICTIONARY.get(self.type)}, "{self.name} = {self.value}" at {id(self)})>'

    def _evaluate(self):
        assert self.type == EXPRESSION
        self.value = eval(self.value)
        self.type = NUMBER