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
        global i
        # Rule: [S]
        if char != '[' \
            or self.S(self.next()) != 1 \
            or self.next() != ']':
                return 0
        if self.ifnext() == 1: #If something exists after T
            print i
            print self.next()
            return 0
        else:
            return 1
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
                i = start
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
                i = start
                return 0
            else:
                return 1
        # Rule: expr
        if self.expr(char) != 1:
            i = start
        else:
            # Rule: expr S
            char = self.next()
            if char == ']':
                i -= 1
                return 1
            elif self.S(char) != 1:
                i = start
                return 0
            else:
                return 1
        return 0

    def expr(self, char):
        global i
        start = i
        if self.oper(char):
            return 1
        if self.stmts(char):
            return 1
        i = start
        return 0

    def oper(self, char):
        global i
        start = i
        # Rule: [:= name oper]
        if char != '['\
            or self.next() != ':' \
            or self.next() != '=' \
            or self.name(self.next()) \
            or self.oper(self.oper()) \
            or self.next() != ']':
            i = start
        else:
            return 1
        # Rule: [binops oper oper]
        if char != '[' \
            or self.binops(self.next()) != 1 \
            or self.oper(self.next()) != 1 \
            or self.oper(self.next()) != 1 \
            or self.next() != ']':
            i = start
        else:
            return 1
        # Rule: [unops oper]
        if char != '[' \
            or self.unops(self.next()) != 1 \
            or self.oper(self.next()) != 1 \
            or self.next() != ']':
            i = start
        else: return 1
        # Rule: constants
        if self.constants(char) != 1:
            i = start
        else: return 1
        # Rule: name
        if self.name(char) != 1:
            i = start
        else: return 1
        return 0

    def binops(self, char):
        global i
        start = i
        # Check if equal to operators
        if char != '+' and char != '-' and char != '*' and char != '/' and \
             char != '%' and char != '^' and char != '=' and char != ':=':
            i = start
        else: return 1
        # Check if equal to LT GT comparators
        if char != '>' and char != '<' and char != '!=' and char != '<=' \
            and char != '>=':
            i = start
        else:
                return 1
        # Check if or or and
        if char != "or":
            i = start
        else: return 1
        if char != "and":
            i = start
        else: return 1
        return 0

    def unops(self, char):
        global i
        start = i
        # Rule: not
        if char != "not":
            i = start
        else: return 1
        # Rule: sin
        if char != "sin":
            i = start
        else: return 1
        # Rule: cos
        if char != "cos":
            i = start
        else: return 1
        # Rule: tan
        if char != "tan":
            i = start
        else: return 1
        return 0

    def constants(self, char):
        global i
        start = i
        # Rule: strings
        if self.strings(char) != 1:
            i = start
        else: return 1
        # Rule: ints
        if self.ints(char) != 1:
            i = start
        else: return 1
        # Rule: floats
        if self.floats(char) != 1:
            i = start
        else: return 1
        return 0


    def strings(self, char):
        global i
        start = i
        char = tokens[i][1]
        # Check for begninning quot mark
        if char != "STRING": #if scanner did not determine string valid via reg expressions
            return 0
        else:
            return 1

    def name(self, char):
        global i
        start = i
        char = tokens[i][1]
        # Check for begninning quot mark
        if char != "IDENTIFIER": #if scanner did not determine name valid via reg expressions
            return 0
        else:
            return 1

    def ints(self, char):
        global i
        start = i
        char = tokens[i][1]
        # Check for begninning quot mark
        if char != "NUMBER": #if scanner did not determine int valid via reg expressions
            return 0
        else:
            return 1

    def floats(self, char):
        global i
        start = i
        char = tokens[i][1]
        # Check for begninning quot mark
        if char != "FLOAT": #if scanner did not determine string valid via reg expressions
            return 0
        else:
            return 1

    def stmts(self, char):
        global i
        start = i
        # Rule: ifstmts
        if self.ifstmts(char) != 1:
            i = start
        else: return 1
        # Rule: whilestmts
        if self.whilestmts(char) != 1:
            i = start
        else: return 1
        # Rule: letstmts
        if self.letstmts(char) != 1:
            i = start
        else: return 1
        # Rule: printstmts
        if self.printstmts(char) != 1:
            i = start
        else: return 1
        return 0

    def printstmts(self, char):
        global i
        start = i
        # Rule: [stdout oper]
        if char != '[' or self.next() != "stdout" or self.oper(self.next()) != 1 \
            or self.next() != ']':
            i = start
        else:
            return 1
        return 0

    def ifstmts(self, char):
        global i
        start = i
        # Rule: [if expr expr expr]
        if char != '[' or self.next() != "if" or self.expr(self.next()) != 1 \
            or self.expr(self.next()) != 1 or self.expr(self.next()) != 1 or self.next() != ']':
            i = start
        else: return 1
        # Rule: [if expr expr]
        if char != '[' or self.next() != "if" or self.expr(self.next()) != 1 or self.expr(self.next()) != 1 \
            or self.next() != ']':
            i = start
        else: return 1
        return 0

    def whilestmts(self, char):
        global i
        start = i
        # Rule: [while expr exprlist]
        if char != '[' or self.next() != "while" or self.expr(self.next()) != 1 \
            or self.exprlist(self.next()) != 1 or self.next() != ']':
            i = start
        else: return 1
        return 0

    def exprlist(self, char):
        global i
        start = i
        # Rule: expr exprlist
        if self.expr(char) != 1 or self.exprlist(self.next()) != 1:
            i = start
        else: return 1
        # Rule: expr
        if self.expr(char) != 1:
            i = start
        else: return 1
        return 0

    def letstmts(self, char):
        global i
        start = i
        # Rule: [let [varlist]]
        if char != '[' or self.next() != "let" or self.next() != '[' \
            or self.varlist(self.next()) != 1 or self.next() != ']' or self.next() != ']':
            i = start
        else: return 1
        return 0

    def varlist(self, char):
        global i
        start = i
        # Rule: [name type] varlist
        if char != '[' or self.name(self.next()) != 1 or self.type(self.next()) != 1 \
            or self.next() != ']' or self.varlist(self.next()) != 1:
            i = start
        else: return 1
        # Rule: [name type]
        if char != '[' or self.name(self.next()) != 1 or self.type(self.next()) != 1 \
            or self.next() != ']':
            i = start
        else: return 1
        return 0

    def type(self, char):
        global i
        start = i
        # Rule: bool
        if char != "bool":
            i = start
        else: return 1
        # Rule: int
        if char != "int":
            i = start
        else: return 1
        # Rule: float
        if char != "float":
            i = start
        else: return 1
        # Rule: string
        if char != "string":
            i = start
        else: return 1
        return 0

    def ifnext(self):
        global tokens
        global i
        if (i + 1) >= len(tokens):
            return 0
        return 1

    def next(self):
        global tokens
        global i
        if self.ifnext():
            i += 1
            return tokens[i][0]
        # Expected character does not exist
        return ''


if __name__ == '__main__':
    print("This is the parser.py file")
    print("This is a helper file to the main.py of Milestone #3 for CS 480")
