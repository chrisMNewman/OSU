# -----------------------------------------------
# file          : lexical_analyzer.py
# author        : Sang Shin | Chris Newman
# date          : 02-13-2014
# class         : CS 480 | Milestone #3
# description   : Contains the Lexer class that 
#                 performs all regex-based lexer
#                 or tokenization
# -----------------------------------------------
#!/usr/bin/python

token_table = []

class Lexer(object):
    ''' A simple regex-based lexer/tokenizer '''
    def __init__(self, skip_whitespace=True):
        pass

    def tokenize(self, character_buffer):
        ''' Manipulate all characters into tokens '''
        self.character_buffer = character_buffer
        skip_next_iteration = False
        skip_mult_iteration = 0
        
        for i in xrange(len(self.character_buffer)):
            word = ''
            is_number_float = False
            is_string_complete = False
            is_id_complete = False
            
            if skip_next_iteration == True:
                skip_next_iteration = False
                continue
            
            if skip_mult_iteration != 0:
                skip_mult_iteration -= 1
                continue
            
            # ---------------------------------------------------------------------------
            # REGEX FOR DELIMITERS
            if self.character_buffer[i] == '{' or \
                    self.character_buffer[i] == '}' or \
                    self.character_buffer[i] == '[' or \
                    self.character_buffer[i] == ']' or \
                    self.character_buffer[i] == '(' or \
                    self.character_buffer[i] == ')':
                        token_table.append([self.character_buffer[i], "DELIMITER"])
                        continue

            # ---------------------------------------------------------------------------
            # REGEX FOR OPERATORS
            if self.character_buffer[i] == '+' or \
                    self.character_buffer[i] == '-' or \
                    self.character_buffer[i] == '*' or \
                    self.character_buffer[i] == '/' or \
                    self.character_buffer[i] == '%' or \
                    self.character_buffer[i] == '^' or \
                    self.character_buffer[i] == '=':
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
                skip_next_iteration = True
            
            # Regex for :=
            if self.character_buffer[i] == ':' and self.character_buffer[i+1] == '=':
                token_table.append([self.character_buffer[i] + self.character_buffer[i+1], "OPERATOR"])
                skip_next_iteration = True

            # ---------------------------------------------------------------------------
            # REGEX FOR STRINGS
            if self.character_buffer[i] == '"':
                start_idx = i
                i += 1
                while is_string_complete == False:
                    if self.character_buffer[i] != '"':
                        word = word + self.character_buffer[i]            
                    else:
                        is_string_complete = True

                    i += 1

                end_idx = i
                skip_mult_iteration = end_idx - start_idx - 1
                token_table.append([word, "STRING"])
                continue

            # ---------------------------------------------------------------------------
            # REGEX FOR IDENTIFIERS/KEYWORDS
            if self.character_buffer[i].isalpha():
                start_idx = i
                while is_id_complete == False:
                    if self.character_buffer[i].isalpha():
                        word = word + self.character_buffer[i]
                        i += 1
                    elif self.character_buffer[i] == '_':
                        word = word + self.character_buffer[i]
                        i += 1
                    elif self.character_buffer[i].isdigit():
                        word = word + self.character_buffer[i]
                        i += 1
                    else:
                        is_id_complete = True
                
                end_idx = i
                skip_mult_iteration = end_idx - start_idx - 1
            
            if word == 'or' or \
                    word == 'and' or \
                    word == 'not' or \
                    word == 'sin' or \
                    word == 'cos' or \
                    word == 'tan' or \
                    word == 'int' or \
                    word == 'bool' or \
                    word == 'float' or \
                    word == 'string' or \
                    word == 'if' or \
                    word == 'while' or \
                    word == 'let' or \
                    word == 'stdout' or \
                    word == 'true' or \
                    word == 'false':
                token_table.append([word, "KEYWORD"])
            
            elif word:
                token_table.append([word, "IDENTIFIER"])
            
            # ---------------------------------------------------------------------------
            # REGEX FOR FLOATING POINT AND INTEGERS
            if self.character_buffer[i].isdigit():
                start_idx = i
                while self.character_buffer[i].isdigit() or self.character_buffer[i] == '-':
                    word = word + self.character_buffer[i]
                    if self.character_buffer[i+1] == '.' or \
                            self.character_buffer[i+1] == 'e':
                        is_number_float = True
                        word = word + self.character_buffer[i+1]
                        i += 1

                    i += 1

                end_idx = i
                skip_mult_iteration = end_idx - start_idx - 1
                
                if is_number_float == True:
                    token_table.append([word, "FLOAT"])
                else:
                    token_table.append([word, "NUMBER"])
        
            # ---------------------------------------------------------------------------
        return token_table
    
    def universal_print(self, token_table):
        ''' Print out the token table '''
        for token in token_table:
            print(token)

if __name__ == '__main__':
    print("This is the lexical_analyzer.py file")
    print("This is a helper file to the main.py of Milestone #2 for CS 480")
