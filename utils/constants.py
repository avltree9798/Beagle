from utils.beagle_function import (
    print_no_newline,
    println,
    end_program,
    to_string
)
from utils.beagle_types import (
    FUNCTION,
    STRING,
    NUMBER,
    EXPRESSION,
    VARIABLE_ASSIGNMENT,
    ACCESSING_VARIABLE
)

TOKEN_DICTIONARY = {
    FUNCTION            : 'FUNCTION',
    STRING              : 'STRING',
    NUMBER              : 'NUMBER',
    EXPRESSION          : 'EXPRESSION',
    VARIABLE_ASSIGNMENT : 'VARIABLE_ASSIGNMENT',
    ACCESSING_VARIABLE  : 'ACCESSING_VARIABLE'
}

OPERATION_SYMBOLS = (
    '+',
    '-',
    '*',
    '/',
    '%',
    '(',
    ')',
    '^'
)

functions = {
    'println'   : println,
    'print'     : print_no_newline,
    'exit'      : end_program,
    'str'       : to_string,
}