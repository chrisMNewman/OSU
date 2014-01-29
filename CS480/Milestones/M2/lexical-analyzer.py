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
        for i in xrange(len(self.character_buffer)):
            if skip_next_iteration == True:
                skip_next_iteration = False
                continue

            if self.character_buffer[i] == '{' or \
                    self.character_buffer[i] == '}' or \
                    self.character_buffer[i] == '[' or \
                    self.character_buffer[i] == ']' or \
                    self.character_buffer[i] == '(' or \
                    self.character_buffer[i] == ')':
                        token_table.append([self.character_buffer[i], "DELIMITER"])
                        continue

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
