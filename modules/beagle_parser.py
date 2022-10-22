from modules.beagle_token import BeagleToken
from utils.beagle_types import (
    FUNCTION,
    EXPRESSION,
    VARIABLE_ASSIGNMENT,
    ACCESSING_VARIABLE
)
from utils.runtime import variables
from utils.constants import functions

class BeagleParser:
    def __init__(self, lexer):
        self.lexer = lexer

    def parse(self, interactive_shell=False):
        tokens_all_lines = self.lexer.tokens
        for token_per_line in tokens_all_lines:
            token_count = len(token_per_line)
            i = token_count-1
            args = []
            while i >= 0:
                curr_token = token_per_line[i]
                if curr_token.type == FUNCTION:
                    function = functions.get(curr_token.value)
                    retval = function(args)
                    args = []
                    args.append(retval)
                elif curr_token.type == EXPRESSION:
                    curr_token._evaluate()
                    args.append(curr_token)
                elif curr_token.type == VARIABLE_ASSIGNMENT:
                    variables.update({
                        curr_token.name: curr_token.value
                    })

                    if interactive_shell:
                        print(curr_token.value.value)
                elif curr_token.type == ACCESSING_VARIABLE:
                    variable = variables.get(curr_token.value)
                    args.append(variable)
                    if interactive_shell:
                        print(variable)
                else:
                    args.append(token_per_line[i])
                i-=1