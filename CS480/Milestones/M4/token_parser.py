# -----------------------------------------------
# file          : parser.py
# author        : Sang Shin | Chris Newman
# date          : 02-20-2014
# class         : CS 480 | Milestone #4
# description   : Contains the Parser class that 
#                 performs all analysis of a string
#                 of symbols according to the rules
#                 of a formal grammar
# -----------------------------------------------
#!/usr/bin/python
import sys

PASS = "PASS"
FAIL = "FAIL"

class Parser(object):
    ''' A simple parser that performs all analysis of a string of symbols '''
    def __init__(self, idx = 0, token_list = []):
        self.idx = idx
        self.token_list = token_list
    
    def parse(self, token_list):
        self.idx = 0
        self.token_list = token_list
        
        if not self.token_list:
            return FAIL
        
        else:
            return self.T(self.token_list[0][0])

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     T = [S]
    def T(self, char):
        # Rule: [S]
        if char != '[' \
                or self.S(self.next()) != PASS \
                or self.next() != ']':
                    return FAIL
        
        # If something exists after T
        if self.ifnext() == PASS:
            return FAIL
        
        else:
            return PASS

        return PASS

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     S = [ ] | [S] | SS | expr
    def S(self, char):
        start = self.idx
        
        # Rule: []
        if char != '[' \
            or self.next() != ']':
                self.idx = start

        # Rule: []S
        else:
            char = self.next()
            if char == ']':
                self.idx -= 1
                return PASS
            
            if self.S(char) != PASS:
                self.idx = start
                return FAIL
            
            else:
                return PASS

        # Rule: [S]
        if char != '[' \
                or not self.S(self.next()) \
                or self.next() != ']':
                    self.idx = start
        
        # Rule: [S]S
        else:
            char = self.next()
            if char == ']':
                self.idx -= 1
                return PASS

            elif self.S(char) != PASS:
                self.idx = start
                return FAIL

            else:
                return PASS

        # Rule: expr
        if self.expr(char) != PASS:
            self.idx = start

        else:
            # Rule: expr S
            char = self.next()
            if char == ']':
                self.idx -= 1
                return PASS

            elif self.S(char) != PASS:
                self.idx = start
                return FAIL

            else:
                return PASS
        
        return FAIL

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     expr = oper | stmts
    def expr(self, char):
        start = self.idx

        if self.oper(char) == PASS:
            return PASS
        
        if self.stmts(char) == PASS:
            return PASS
        
        self.idx = start

        return FAIL

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     oper = [:= name oper] | [binops oper oper] | [unops oper] |
    #                           constants | name
    def oper(self, char):
        start = self.idx
        
        # Rule: [:= name oper]
        if char != '['\
                or self.next() != ':' \
                or self.next() != '=' \
                or self.name(self.next()) \
                or self.oper(self.oper()) \
                or self.next() != ']':
                    self.idx = start
        
        else:
            return PASS
        
        # Rule: [binops oper oper]
        if char != '[' \
                or self.binops(self.next()) != PASS \
                or self.oper(self.next()) != PASS \
                or self.oper(self.next()) != PASS \
                or self.next() != ']':
                    self.idx = start
        
        else:
            return PASS
        
        # Rule: [unops oper]
        if char != '[' \
                or self.unops(self.next()) != PASS \
                or self.oper(self.next()) != PASS \
                or self.next() != ']':
                    self.idx = start
        
        else: 
            return PASS
        
        # Rule: constants
        if self.constants(char) != PASS:
            self.idx = start

        else: 
            return PASS

        # Rule: name
        if self.name(char) != PASS:
            self.idx = start

        else: 
            return PASS
        
        return FAIL
    
    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     binops = + | - | * | / | % | ^ | = | > | >= | < | <= | != | or | and
    def binops(self, char):
        start = self.idx

        # Check if equal to operators
        if char != '+' \
                and char != '-' \
                and char != '*' \
                and char != '/' \
                and char != '%' \
                and char != '^' \
                and char != '=' \
                and char != ':=':
                    self.idx = start
       
        else: 
            return PASS

        # Check if equal to LT GT comparators
        if char != '>' \
                and char != '<' \
                and char != '!=' \
                and char != '<=' \
                and char != '>=':
                    self.idx = start

        else:
                return PASS

        # Check if or or and
        if char != "or":
            self.idx = start

        else: 
            return PASS

        if char != "and":
            self.idx = start

        else: 
            return PASS
        
        return FAIL

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     unops = - | not | sin | cos | tan
    def unops(self, char):
        start = self.idx

        #Rule: -
        if char != '-':
            self.idx = start
        
        else:
            return PASS

        # Rule: not
        if char != "not":
            self.idx = start

        else: 
            return PASS

        # Rule: sin
        if char != "sin":
            self.idx = start

        else: 
            return PASS

        # Rule: cos
        if char != "cos":
            self.idx = start

        else: 
            return PASS

        # Rule: tan
        if char != "tan":
            self.idx = start

        else: 
            return PASS
        
        return FAIL

    # -------------------------------------------------------------------------
    # GRAMMAR RULE =    constants = strings | ints | floats
    def constants(self, char):
        start = self.idx

        # Rule: strings
        if self.strings(char) != PASS:
            self.idx = start

        else: 
            return PASS

        # Rule: ints
        if self.ints(char) != PASS:
            self.idx = start

        else: 
            return PASS

        # Rule: floats
        if self.floats(char) != PASS:
            self.idx = start

        else: 
            return PASS

        return FAIL

    # -------------------------------------------------------------------------
    # TERMINAL:         Reg_ex for string literal in C
    def strings(self, char):
        start = self.idx
        char = self.token_list[self.idx][1]

        if char != "STRING":
            return FAIL
        
        else:
            return PASS

    # -------------------------------------------------------------------------
    # TERMINAL:         Reg_ex for identifiers in C
    def name(self, char):
        start = self.idx
        char = self.token_list[self.idx][1]
        
        if char != "IDENTIFIER":
            return FAIL
        
        else:
            return PASS

    # -------------------------------------------------------------------------
    # TERMINAL:         Reg_ex for positive/negative ints in C
    def ints(self, char):
        start = self.idx
        char = self.token_list[self.idx][1]
        
        if char != "NUMBER":
            return FAIL
        
        else:
            return PASS

    # -------------------------------------------------------------------------
    # TERMINAL:         Reg_ex for positive/negative doubles in C
    def floats(self, char):
        start = self.idx
        char = self.token_list[self.idx][1]
        
        if char != "FLOAT":
            return FAIL
        
        else:
            return PASS

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     stmts = ifstmts | whilestmts | letstmts | printstmts
    def stmts(self, char):
        start = self.idx

        # Rule: ifstmts
        if self.ifstmts(char) != PASS:
            self.idx = start

        else: 
            return PASS

        # Rule: whilestmts
        if self.whilestmts(char) != PASS:
            self.idx = start

        else: 
            return PASS

        # Rule: letstmts
        if self.letstmts(char) != PASS:
            self.idx = start

        else: 
            return PASS

        # Rule: printstmts
        if self.printstmts(char) != PASS:
            self.idx = start
        
        else: 
            return PASS
        
        return FAIL

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     printstmts = [stdout oper]
    def printstmts(self, char):
        start = self.idx

        # Rule: [stdout oper]
        if char != '[' \
                or self.next() != "stdout" \
                or self.oper(self.next()) != PASS \
                or self.next() != ']':
                    self.idx = start
        
        else:
            return PASS

        return FAIL

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     ifstmts = [if expr expr expr] | [if expr expr]
    def ifstmts(self, char):
        start = self.idx

        # Rule: [if expr expr expr]
        if char != '[' \
                or self.next() != "if" \
                or self.expr(self.next()) != PASS \
                or self.expr(self.next()) != PASS \
                or self.expr(self.next()) != PASS \
                or self.next() != ']':
                    self.idx = start

        else: 
            return PASS

        # Rule: [if expr expr]
        if char != '[' \
                or self.next() != "if" \
                or self.expr(self.next()) != PASS \
                or self.expr(self.next()) != PASS \
                or self.next() != ']':
                    self.idx = start
        
        else: 
            return PASS

        return FAIL

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     whilestmts = [while expr exprlist]
    def whilestmts(self, char):
        start = self.idx

        # Rule: [while expr exprlist]
        if char != '[' \
                or self.next() != "while" \
                or self.expr(self.next()) != PASS \
                or self.exprlist(self.next()) != PASS \
                or self.next() != ']':
                    self.idx = start

        else: 
            return PASS
        
        return FAIL

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     exprlist = expr | expr exprlist
    def exprlist(self, char):
        start = self.idx

        # Rule: expr exprlist
        if self.expr(char) != PASS \
                or self.exprlist(self.next()) != PASS:
                    self.idx = start

        else: 
            return PASS

        # Rule: expr
        if self.expr(char) != PASS:
            self.idx = start

        else: 
            return PASS

        return FAIL

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     letstmts = [let [varlist]]
    def letstmts(self, char):
        start = self.idx

        # Rule: [let [varlist]]
        if char != '[' \
                or self.next() != "let" \
                or self.next() != '[' \
                or self.varlist(self.next()) != PASS \
                or self.next() != ']' \
                or self.next() != ']': 
                    self.idx = start

        else: 
            return PASS

        return FAIL

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     varlist = [name type] | [name type] varlist
    def varlist(self, char):
        start = self.idx

        # Rule: [name type] varlist
        if char != '[' \
                or self.name(self.next()) != PASS \
                or self.type(self.next()) != PASS \
                or self.next() != ']' \
                or self.varlist(self.next()) != PASS:
                    self.idx = start

        else: 
            return PASS
        
        # Rule: [name type]
        if char != '[' \
                or self.name(self.next()) != PASS \
                or self.type(self.next()) != PASS \
                or self.next() != ']':
                    self.idx = start

        else: 
            return PASS
        
        return FAIL

    # -------------------------------------------------------------------------
    # GRAMMAR RULE:     type = bool | int | float
    def type(self, char):
        start = self.idx

        # Rule: bool
        if char != "bool":
            self.idx = start

        else: 
            return PASS

        # Rule: int
        if char != "int":
            self.idx = start

        else: 
            return PASS

        # Rule: float
        if char != "float":
            self.idx = start

        else: 
            return PASS

        # Rule: string
        if char != "string":
            self.idx = start

        else: 
            return PASS
        
        return FAIL

    # -------------------------------------------------------------------------
    # HELPER FUNCTIONS
    def ifnext(self):
        if (self.idx + 1) >= len(self.token_list):
            return FAIL
        
        return PASS

    def next(self):
        if self.ifnext() == PASS:
            self.idx += 1
            return self.token_list[self.idx][0]

        # Expected character does not exist
        return ''

if __name__ == '__main__':
    print("This is the token_parser.py file")
    print("This is a helper file to the main.py of Milestone #4 for CS 480")
