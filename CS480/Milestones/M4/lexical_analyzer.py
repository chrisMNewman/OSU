# -----------------------------------------------
# file          : lexical_analyzer.py
# author        : Sang Shin | Chris Newman
# date          : 02-13-2014
# class         : CS 480 | Milestone #4
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
        scope = 0
        Sindx = 0
        
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
            # REGEX FOR FRONT DELIMITERS
            if self.character_buffer[i] == '{' or \
                    self.character_buffer[i] == '[' or \
                    self.character_buffer[i] == '(':
                        scope += 1
                        if scope == 2:
                            Sindx += 1
                        token_table.append([self.character_buffer[i], "DELIMITER", scope, Sindx])
                        continue

             # ---------------------------------------------------------------------------
            # REGEX FOR BACK DELIMITERS
            if self.character_buffer[i] == '}' or \
                    self.character_buffer[i] == ']' or \
                    self.character_buffer[i] == ')':
                        token_table.append([self.character_buffer[i], "DELIMITER", scope, Sindx])
                        scope -= 1
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
                        token_table.append([self.character_buffer[i], "OPERATOR", scope, Sindx])
                        continue

            # Regex for < and <=
            if self.character_buffer[i] == '<' and self.character_buffer[i+1] == '=':
                token_table.append([self.character_buffer[i] + self.character_buffer[i+1], "OPERATOR", scope, Sindx])
                skip_next_iteration = True

            elif self.character_buffer[i] == '<' and self.character_buffer[i+1] != '=':
                token_table.append([self.character_buffer[i], "OPERATOR", scope, Sindx])

            # Regex for > and >=
            if self.character_buffer[i] == '>' and self.character_buffer[i+1] == '=':
                token_table.append([self.character_buffer[i] + self.character_buffer[i+1], "OPERATOR", scope, Sindx])
                skip_next_iteration = True

            elif self.character_buffer[i] == '>' and self.character_buffer[i+1] != '=':
                token_table.append([self.character_buffer[i], "OPERATOR", scope, Sindx])
            
            # Regex for !=
            if self.character_buffer[i] == '!' and self.character_buffer[i+1] == '=':
                token_table.append([self.character_buffer[i] + self.character_buffer[i+1], "OPERATOR", scope, Sindx])
                skip_next_iteration = True
            
            # Regex for :=
            if self.character_buffer[i] == ':' and self.character_buffer[i+1] == '=':
                token_table.append([self.character_buffer[i] + self.character_buffer[i+1], "OPERATOR", scope, Sindx])
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
                token_table.append([word, "STRING", scope, Sindx])
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
                token_table.append([word, "KEYWORD", scope, Sindx])
            
            elif word:
                token_table.append([word, "IDENTIFIER", scope, Sindx])
            
            # ---------------------------------------------------------------------------
            # REGEX FOR FLOATING POINT AND INTEGERS
            if self.character_buffer[i].isdigit() or self.character_buffer[i] == '.':
                start_idx = i
                dot_num = 0 #Number of .'s in number (should be one or less)
                e_num = 0 #Number of e's in number (should be one or less)
                if self.character_buffer[i] == '.': #If float starts with '.'
                    dot_num += 1
                while self.character_buffer[i].isdigit() or self.character_buffer[i] == '-' \
                        or self.character_buffer[i] == '.':
                    word = word + self.character_buffer[i]
                    if self.character_buffer[i+1] == '.':
                        is_number_float = True
                        dot_num += 1
                        if dot_num > 1:
                            i += 1
                            break
                        else:
                            word = word + self.character_buffer[i+1]
                            i += 1

                    if self.character_buffer[i+1] == 'e':
                        is_number_float = True
                        e_num += 1
                        if e_num > 1:
                            i += 1
                            break
                        else:
                            word = word + self.character_buffer[i+1]
                            i += 1

                    i += 1

                end_idx = i
                skip_mult_iteration = end_idx - start_idx - 1
                
                if is_number_float == True:
                    token_table.append([word, "FLOAT", scope, Sindx])
                else:
                    token_table.append([word, "NUMBER", scope, Sindx])
        
            # ---------------------------------------------------------------------------
        return token_table
    
    def universal_print(self, token_table):
        ''' Print out the token table '''
        for token in token_table:
            print(token)

if __name__ == '__main__':
    print("This is the lexical_analyzer.py file")
    print("This is a helper file to the main.py of Milestone #4 for CS 480")
