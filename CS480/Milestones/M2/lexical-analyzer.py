# -------------------------------------
# file      : lexical-analyzer.py
# date      : 01-27-2014
# member    : Sang Shin | Chris Newman 
# class     : CS 480
# Assign    : Milestone #2
# -------------------------------------
#!/usr/bin/python

type_names = [
        "NAME",
        "NUMBER",
        "STRING",
        "NEWLINE",
        "LPAR",
        "RPAR",
        "COLON",
        "COMMA",
        "SEMI",
        "PLUS",
        "MINUS",
        "STAR",
        "SLASH",
        "VBAR",
        "AMPER",
        "LESS",
        "GREATER",
        "EQUAL",
        "DOT",
        "PERCENT",
        "BACKQUOTE",
        "LBRACE",
        "RBRACE",
        "EQEQUAL",
        "NOTEQUAL",
        "LESSEQUAL",
        "GREATEREQUAL",
        "TILDE",
        "CIRCUMFLEX",
        "LEFTSHIFT",
        "RIGHTSHIFT",
        "DOUBLESTAR",
        "PLUSEQUAL",
        "MINEQUAL",
        "STAREQUAL",
        "SLASHEQUAL",
        "PERCENTEQUAL",
        "AMPEREQUAL",
        "VBAREQUAL",
        "CIRCUMFLEXEQUAL",
        "LEFTSHIFTEQUAL",
        "RIGHTSHIFTEQUAL",
        "DOUBLESTAREQUAL",
        "DOUBLESLASH",
        "DOUBLESLASHEQUAL",
        "AT"
        ]

rules = [
        ('\d+',             'NUMBER'),
        ('[a-zA-Z_]\w*',    'IDENTIFIER'),
        ('\+',              'PLUS'),
        ('\-',              'MINUS'),
        ('\*',              'MULTIPLY'),
        ('\/',              'DIVIDE'),
        ('\(',              'LPAREN'),
        ('\)',              'RPAREN'),
        ('=',               'EQUALS'),
        ]

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
