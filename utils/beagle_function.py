from utils.beagle_types import STRING
import sys

def print_no_newline(token):
    data = token
    if isinstance(data, list) and len(data)>0:
        data = data[0]
    
    if hasattr(data, 'value'):
        data = data.value
    assert isinstance(data, str)
    if data:
        sys.stdout.write(data)
        
def println(token_array):
    assert len(token_array) == 1
    print_no_newline(token_array[0])
    print_no_newline('\n')

def end_program(retval=0):
    exit(retval)

def to_string(token_array):
    assert len(token_array) == 1
    token_array[0].type = STRING
    token_array[0].value = str(token_array[0].value)
    return token_array[0]



