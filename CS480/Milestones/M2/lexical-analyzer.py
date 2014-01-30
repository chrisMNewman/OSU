#!/usr/bin/python
import sys

# Global Constants
FILE_NAME = "example-c-file.c"

character_buffer = []
token_table = []

class Lexer(object):
    def __init__(self, skip_whitespace=True):
        pass

    def tokenize(self, character_buffer):
        self.character_buffer = character_buffer
        skip_next_iteration = False
        skip_mult_iteration = 0
        for i in xrange(len(self.character_buffer)):
            word = ''

            if skip_next_iteration == True:
                skip_next_iteration = False
                continue
            
            if skip_mult_iteration != 0:
                skip_mult_iteration -= 1
                continue
            
            # Regex for delimiters
            if self.character_buffer[i] == '{' or \
                    self.character_buffer[i] == '}' or \
                    self.character_buffer[i] == '[' or \
                    self.character_buffer[i] == ']' or \
                    self.character_buffer[i] == '(' or \
                    self.character_buffer[i] == ')':
                        token_table.append([self.character_buffer[i], "DELIMITER"])
                        continue
            
            # Regex for operators
            if self.character_buffer[i] == '+' or \
                    self.character_buffer[i] == '-' or \
                    self.character_buffer[i] == '*' or \
                    self.character_buffer[i] == '/' or \
                    self.character_buffer[i] == '%' or \
                    self.character_buffer[i] == '=' or \
                    self.character_buffer[i] == '#' or \
                    self.character_buffer[i] == '%' or \
                    self.character_buffer[i] == 'and' or \
                    self.character_buffer[i] == 'or':
                        token_table.append([self.character_buffer[i], "OPERATOR"])
                        continue

            # Regex for < and <=
            if self.character_buffer[i] == '<' and self.character_buffer[i+1] == '=':
                token_table.append([self.character_buffer[i] + self.character_buffer[i+1], "OPERATOR"])
                skip_next_iteration = True

            elif self.character_buffer[i] == '<' and self.character_buffer[i+1] != '=':
                token_table.append([self.character_buffer[i], "OPERATOR"])

            # Regex for > and >=
            if self.character_buffer[i] == '>' and self.character_buffer[i+1] == '=':
                token_table.append([self.character_buffer[i] + self.character_buffer[i+1], "OPERATOR"])
                skip_next_iteration = True

            elif self.character_buffer[i] == '>' and self.character_buffer[i+1] != '=':
                token_table.append([self.character_buffer[i], "OPERATOR"])
            
            # Regex for !=
            if self.character_buffer[i] == '!' and self.character_buffer[i+1] == '=':
                token_table.append([self.character_buffer[i] + self.character_buffer[i+1], "OPERATOR"])
                skip_next_iteration = True

            # Regex for alpha characters
            if self.character_buffer[i].isalpha():
                start_idx = i
                while self.character_buffer[i].isalpha():
                    word = word + self.character_buffer[i]
                    i += 1
                
                end_idx = i
                skip_mult_iteration = end_idx - start_idx - 1
            
            # Check for keywords. If not, then it must be an identifier
            if word == 'include' or \
                    word == 'not' or \
                    word == 'sin' or \
                    word == 'cos' or \
                    word == 'tan' or \
                    word == 'int' or \
                    word == 'bool' or \
                    word == 'float' or \
                    word == 'string' or \
                    word == 'if' or \
                    word == 'while' or \
                    word == 'let' or \
                    word == 'stdout':
                token_table.append([word, "KEYWORD"])
            
            elif word.isalpha():
                token_table.append([word, "IDENTIFIER"])
            
            # Regex for digit numbers
            if self.character_buffer[i].isdigit():
                start_idx = i
                while self.character_buffer[i].isdigit():
                    word = word + self.character_buffer[i]
                    i += 1
                end_idx = i
                skip_mult_iteration = end_idx - start_idx - 1

                token_table.append([word, "NUMBER"])

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
    initialize(FILE_NAME)
    lx = Lexer()
    lx.tokenize(character_buffer)
    lx.universal_print(token_table)

if __name__ == '__main__':
    main()
