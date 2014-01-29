# -------------------------------------
# file      : lexical-analyzer.py
# date      : 01-27-2014
# member    : Sang Shin | Chris Newman 
# class     : CS 480
# Assign    : Milestone #2
# -------------------------------------
#!/usr/bin/python

terms = {
        'sin'       : 'TRIG',
        'cos'       : 'TRIG',
        'tan'       : 'TRIG',
        'stdout'    : 'PRINTSTMT',
        'if'        : 'IFSTMT',
        'while'     : 'WHILESTMT',
        'true'      : 'BOOLEAN',
        'false'     : 'BOOLEAN',
        'not'       : 'NOT',
        'or'        : 'OR',
        'and'       : 'AND',
        }

rules = {
        '\d+'           : 'NUMBER',
        '\d+.\d+'       : 'FLOAT',
        '[a-zA-Z_]\w*'  : 'IDENTIFIER',
        '\+'            : 'PLUS',
        '\-'            : 'MINUS',
        '\*'            : 'MULTIPLY',
        '\/'            : 'DIVIDE',
        '\%'            : 'MODULUS',
        '\^'            : 'CAROT',
        '\:='           : 'ASSIGNMENTEQUAL',
        '\('            : 'LPAREN',
        '\)'            : 'RPAREN',
        '\['            : 'LBRACK',
        '\]'            : 'RBRACK',
        '='             : 'EQUALS',
        }

class Token(object):
    '''
    Token Structure.
    Input: typ, val, pos
    '''
    def __init__(self, typ, val, pos):
        self.typ = typ
        self.val = val
        self.pos = pos

    def __str__(self):
        return '<%s, %s, %s>' % (self.typ, self.val, self.pos)

class Lexer(object):
    def __init__(self, rules, terms, skip_whitespace=True):
        self.rules = []
        self.terms = []
        self.skip_whitespace = skip_whitespace

class LexerError(Exception):
    def __init__(self, pos):
        self.pos = pos
