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
        "BOOLEAN",
        "STRING",
        "NEWLINE",
        "LPAREN",
        "RPAREN",
        "LBRACK",
        "RBRACK",
        "COLON",
        "COMMA",
        "SEMICOLON",
        "PLUS",
        "MINUS",
        "STAR",
        "SLASH",
        "MODULUS",
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
        "AT",
        "OP",
        "<ERRORTOKEN>",
        "<N_TOKENS>"
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
        ('\[',              'LBRACK'),
        ('\]',              'RBRACK'),
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
