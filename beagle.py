from modules.beagle_parser import BeagleParser
from modules.lexer import Lexer

import sys

VERSION = '0.0.1'

def execute_file(filename):
    data = ""
    try:
        with open(filename, 'r') as f:
            data = f.read()
    except:
        print("[-] Failed to open file {filename}".format(filename=filename))
        exit(1)
        
    lexer = Lexer(data)
    lexer.lex()
    parser = BeagleParser(lexer)
    parser.parse()

def interactive_shell():
    user_input = ''
    still_running = True
    while still_running:
        user_input = input(f'Beagle {VERSION} >> ')
        if user_input == 'exit':
            still_running = False
        else:
            lexer = Lexer(user_input)
            lexer.lex()
            parser = BeagleParser(lexer)
            parser.parse(interactive_shell=True)
            lexer = None
            parser = None
            del lexer
            del parser
    

def main(argc, argv):
    if argc == 2:
        execute_file(argv[1])
        exit(0)
    interactive_shell()

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)