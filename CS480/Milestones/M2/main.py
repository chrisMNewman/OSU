# -----------------------------------------------
# file          : main.py
# author        : Sang Shin | Chris Newman
# date          : 01-30-2014
# class         : CS 480 | Milestone #2
# description   : Primary execution file
# -----------------------------------------------
#!/usr/bin/python
import sys
import lexical_analyzer as lx

# Global Constants
FILE_NAME = ''

character_buffer = []

def initialize(filename):
    ''' Initialize by reading in the file and splitting all strings into characters '''
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                for character in line:
                    character_buffer.append(character)

    except IOError:
        print("Could not read file:", filename)
        sys.exit()

def main():
    FILE_NAME = raw_input("Enter Filename: ")
    initialize(FILE_NAME)
    token_table = lx.Lexer().tokenize(character_buffer)
    lx.Lexer().universal_print(token_table)

if __name__ == '__main__':
    main()
