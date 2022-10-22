from modules.beagle_token import BeagleToken, RESERVED_KEYWORDS
from utils.constants import (
    OPERATION_SYMBOLS,
)
from utils.runtime import variables
from utils.beagle_types import (
    FUNCTION,
    STRING,
    NUMBER,
    EXPRESSION,
    VARIABLE_ASSIGNMENT,
    ACCESSING_VARIABLE
)

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
    
    def _check_previous_token(self, previous_token, line):
        function_name = previous_token.strip()
        if function_name.endswith('"'):
            function_name = function_name[:-1]
        if function_name != '':
            print(f'[-] Function {function_name.strip()} on line {line+1} does not exists in the Beagle Program.\nExiting.\n')
            exit(1)

    def lex(self):
        code_by_lines = self.code.split("\n")
        temp_variable_names = set()
        for i, line in enumerate(code_by_lines):
            token = ''
            state = 0
            string = ''
            beagle_tokens = []
            expression = ''
            number = ''
            variable_name = ''
            variable_value = ''
            found_operation = False
            for j, tok in enumerate(line):
                token += tok
                if tok == '=' and state == 0 and variable_name == '':
                    token = token.strip()[:-1]
                    variable_name = token
                    token = ''
                elif token == ' ' and state == 0:
                    token = ''
                elif token == '#' and state == 0:
                    break
                elif token in RESERVED_KEYWORDS and (j+1 == len(line) or line[j+1] == ' '):
                    beagle_tokens.append(
                        BeagleToken(FUNCTION, token)
                    )
                    token = ''
                elif token in temp_variable_names:
                    beagle_tokens.append(
                        BeagleToken(ACCESSING_VARIABLE, token)
                    )
                elif token in OPERATION_SYMBOLS:
                    found_operation = True
                    expression += token
                    token = ''
                elif token.isdigit():
                    expression += token 
                    token = ''
                elif tok == '"':
                    if state == 0:
                        self._check_previous_token(token, i)
                        state = 1
                    elif state == 1:
                        new_string = BeagleToken(STRING, string)
                        if variable_name == '':
                            beagle_tokens.append(
                                new_string
                            )
                        else:
                            temp_variable_names.add(variable_name)
                            beagle_tokens.append(
                                BeagleToken(VARIABLE_ASSIGNMENT, new_string, variable_name)
                            )
                            variable_name = ''
                        state = 0
                        string = ''
                elif state == 1:
                    string += tok
            
            if expression or found_operation:
                if expression and found_operation:
                    beagle_tokens.append(
                        BeagleToken(EXPRESSION, expression)
                    )
                elif expression and not found_operation and not variable_name:
                    beagle_tokens.append(
                        BeagleToken(NUMBER, expression)
                    )
                else:
                    temp_variable_names.add(variable_name)
                    number = BeagleToken(NUMBER, expression)
                    beagle_tokens.append(
                        BeagleToken(VARIABLE_ASSIGNMENT, number, variable_name)
                    )
            self.tokens.append(beagle_tokens)
