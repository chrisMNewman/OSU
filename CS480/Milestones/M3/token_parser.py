# -----------------------------------------------
# file          : parser.py
# author        : Sang Shin | Chris Newman
# date          : 02-03-2014
# class         : CS 480 | Milestone #3
# description   : Contains the Parser class that 
#                 performs all analysis of a string
#                 of symbols according to the rules
#                 of a formal grammar
# -----------------------------------------------
#!/usr/bin/python

import sys

class Parser(object):
    ''' A simple parser that performs all analysis of a string of symbols '''
    def __init__(self):
            pass

    def parse(self, token_list):
        global i
        global tokens
        i = 0
        tokens = token_list
        print self.T(tokens[0][0])

    def T(self, char):
        # Rule: [S]
        if char != '[' \
            or self.S(self.next()) != 1 \
            or self.next() != ']' \
            or self.ifnext() == 1:
            return 0
        return 1

    def S(self, char):
        global i
        start = i
        # Rule: []
        if char != '[' \
            or self.next() != ']':
            i = start
        # Rule: []S
        else:
            char = self.next()
            if char == ']':
                i -= 1
                return 1
            if self.S(char) != 1:
                return 0
            else:
                return 1
        # Rule: [S]
        if char != '[' \
            or not self.S(self.next()) \
            or self.next() != ']':
            i = start
        # Rule: [S]S
        else:
            char = self.next()
            if char == ']':
                i -= 1
                return 1
            elif self.S(char) != 1:
                return 0
            else:
                return 1
        # Rule: expr
        if self.expr(char) != 1:
            i = start
        else:
            return 1
        return 0

    def expr(self, char):
        if self.oper(char):
            return 1
        if self.stmts(char):
            return 1
        return 0

    def oper(self, char):
        global i
        start = i
        if char != '[':
            return 0
        # Rule: := name oper
        if self.next() != ':' \
            or self.next() != '=' \
            or self.name(self.next()) \
            or self.oper(self.oper()) \
            or self.next() != ']':
            i = start
        else:
            if self.next() == ']':
                return 1
            else: return 0
        # Rule: binops oper oper
        if self.binops(self.next()) != 1 \
            or self.oper(self.next()) != 1 \
            or self.oper(self.next()) != 1:
            i = start
        else:
            if self.next() == ']':
                return 1
            else: return 0
        # Rule: unops oper
        if self.unops(self.next()) != 1 \
            or self.oper(self.next()) != 1:
            i = start
        else:
            if self.next() == ']':
                return 1
            else: return 0
        # Rule: constants
        if self.constants(self.next()) != 1:
            i = start
        else:
            if self.next() == ']':
                return 1
            else: return 0
        # Rule: name
        if self.name(self.next()) != 1:
            i = start
        else:
            if self.next() == ']':
                return 1
            else: return 0
        return 0

    def binops(self, char):
        global i
        start = i
        # Check if equal to operators
        if char != '+' or char != '-' or char != '*' or char != '/' or \
             char != '%' or char != '^' or char != '=':
            i = start
        else: return 1
        # Check if equal to LT GT comparators
        if char != '>' or char != '<' or char != '!':
            i = start
        else:
            if self.next() != '=':
                return 1
            else:
                i -= 1
                return 1
        # Check if or or and
        if char != 'o' or self.next() != 'r':
            i = start
        else: return 1
        if char != 'a' or self.next() != 'n' or self.next() != 'd':
            i = start
        else: return 1
        return 0

    def unops(self, char):
        global i
        start = i
        # Rule: not
        if char != 'n' or self.next() != 'o' or self.next() != 't':
            i = start
        else: return 1
        # Rule: sin
        if char != 's' or self.next() != 'i' or self.next() != 'n':
            i = start
        else: return 1
        # Rule: cos
        if char != 'c' or self.next() != 'o' or self.next() != 's':
            i = start
        else: return 1
        # Rule: tan
        if char != 't' or self.next() != 'a' or self.next() != 'n':
            i = start
        else: return 1

    def stmts(self, char):
        if char == 'b':
            return 1
        return 0

    def ifnext(self):
        global tokens
        global i
        if (i + 1) == len(tokens):
            return 0
        return 1

    def next(self):
        global tokens
        global i
        if self.ifnext():
            i += 1
            print tokens[i][0]
            return tokens[i][0]
        # Expected character does not exist
        return ''

    def back(self, pos):
        global tokens
        global i
        i == pos
        return tokens[i][0]

if __name__ == '__main__':
    print("This is the parser.py file")
    print("This is a helper file to the main.py of Milestone #3 for CS 480")
