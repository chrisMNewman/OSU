#!/usr/bin/python
import sys

operators = [
        '+',
        '-',
        '*',
        '**',
        '/',
        '//',
        '%',
        '<<',
        '>>',
        '&',
        '|',
        '^',
        '~',
        '<',
        '>',
        '<=',
        '>=',
        '==',
        '!=',
        '<>',
        ':=',
        ]

delimiters = [
        '(',
        ')',
        '[',
        ']',
        '{',
        '}',
        '@',
        '#',
        ',',
        ':',
        '.',
        '`',
        '=',
        ';',
        '+=',
        '-=',
        '*=',
        '/=',
        '//=',
        '%=',
        '&=',
        '|=',
        '^=',
        '>>=',
        '<<=',
        '**=',
        ]

keywords = [
        'include',
        'void',
        'printf',
        'stdout',
        'if',
        'while',
        'let',
        'bool',
        'int',
        'float',
        'string',
        ]
                
character_buffer = []
token_table = []

class Lexer(object):
    def __init__(self, operators, delimiters, keywords, skip_whitespace=True):
        self.operators = operators
        self.delimiters = delimiters
        self.keywords = keywords

    def next_input(self, character_buffer):
        self.character_buffer = character_buffer
        for character, next_character in zip(character_buffer, character_buffer[1::]):
            check_operator = self.check_for_operators(character)
            if check_operator == False:
                check_delimiter = self.check_for_delimiters(character)
                if check_delimiter == False:
                    check_keywords = self.check_for_keywords(character)
    
    def check_for_operators(self, character):
        for op in self.operators:
            if op == character:
                token_table.append([character, "OP"])
                return True
            else:
                pass
        return False
    
    def check_for_delimiters(self, character):
        for delim in self.delimiters:
            if delim == character:
                token_table.append([character, "DELIMITER"])
                return True
            else:
                pass
        return False
    
    def check_for_keywords(self, character):
        for word in self.keywords:
            if word == character:
                token_table.append([character, "KEYWORD"])
                return True
            else:
                pass
        return False

    def universal_print(self, token_table):
        for token in token_table:
            print(token)

def initialize(filename):
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                for character in line:
                    character_buffer.append(character)
    except IOError:
        print("Could not read file:", filename)
        sys.exit()

def main():
    initialize("temp.c")
    lx = Lexer(operators, delimiters, keywords)
    lx.next_input(character_buffer)
    lx.universal_print(token_table)

if __name__ == '__main__':
    main()
