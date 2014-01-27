#!/usr/bin/python

class Token(object):
    def __init__(self, typ, val, pos):
        self.typ = typ
        self.val = val
        self.pos = pos

    def __str__(self):
        return '<%s, %s, %s>' % (self.typ, self.val, self.pos)

class LexerError(Exception):
    def __init__(self, pos):
        self.pos = pos
