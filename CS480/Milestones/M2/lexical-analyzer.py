# -------------------------------------
# file      : lexical-analyzer.py
# date      : 01-27-2014
# member    : Sang Shin | Chris Newman 
# class     : CS 480
# Assign    : Milestone #2
# -------------------------------------
#!/usr/bin/python

term_name = {
            'sin'       : 'TRIG',
            'cos'       : 'TRIG',
            'tan'       : 'TRIG',
            'stdout'    : 'PRINTSTMT',
            'if'        : 'IFSTMT',
            'while'     : 'WHILESTMT',
            'true'      : 'BOOLEAN',
            'false'     : 'BOOLEAN',
            }

rules = {
        '\d+'           : 'NUMBER',
        '\d+.\d+'       : 'FLOAT',
        '[a-zA-Z_]\w*'  : 'IDENTIFIER',
        '\!'            : 'NOT',
        '\+'            : 'PLUS',
        '\-'            : 'MINUS',
        '\*'            : 'MULTIPLY',
        '\/'            : 'DIVIDE',
        '\%'            : 'MODULUS',
        '\^'            : 'CAROT',
        '\||'           : 'OR',
        '\&&'           : 'AND',
        '\:='           : 'COLONEQUAL',
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

class LexerError(Exception):
    def __init__(self, pos):
        self.pos = pos
