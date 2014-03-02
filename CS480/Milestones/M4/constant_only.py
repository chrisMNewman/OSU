# -----------------------------------------------
# file          : constant_only.py
# author        : Sang Shin | Chris Newman
# date          : 02-20-2014
# class         : CS 480 | Milestone #4
# description   : Generate gforth code and run 
#                 that code to show the result.
#                 Tests must show that the operations
#                 are correctly implemented based on
#                 their customary definitions in bool,
#                 int, float, and string.
# -----------------------------------------------
#!/usr/bin/python
import stack as s

class Constant_Only(object):
    ''' A simple code generator that takes arithmetic and transforms it into gforth '''
    def __init__(self, token_list = []):
        self.token_list = token_list
    
    def remove_brackets(self):
        ''' Remove the brackets from the token list '''
        idx = 0
        data_list = []
        
        for i in xrange(len(self.token_list)):
            char = self.token_list[idx][0]
            typ = self.token_list[idx][1]
            scope = self.token_list[idx][2]
            Sindx = self.token_list[idx][3]
            
            if char == '[' or char == ']':
                pass

            else:
                data_list.append([char, typ, scope, Sindx])

            idx += 1
        
        return data_list

    def check_floating_point(self, raw_data_list):
        ''' Check to see if the raw_data_list has any floating point numbers '''
        idx = 0
        for i in xrange(len(raw_data_list)):
            typ = raw_data_list[idx][1]
            if typ == 'FLOAT':
                return True
            
            idx += 1

        return False
    
    def check_specific_operator(self, raw_data_list):
        ''' Check to see if the raw_data_list contains a specific operator '''
        idx = 0
        for i in xrange(len(raw_data_list)):
            char = raw_data_list[idx][0]
            if char == '>' or \
                    char == '>=' or \
                    char == '<' or \
                    char == '<=' or \
                    char == '=' or \
                    char == '!=':
                        return True

            idx += 1

        return False
    
    def modify_data(self, raw_data_list, is_floating_point):
        ''' Modify the raw_data_list to check for negate and ^ '''

        # Algorithm for the negate operator
        end_idx = len(raw_data_list) - 1
        counter_operand = 0
        prev_scope = raw_data_list[end_idx][2] # Keep track of scope
        for i in xrange(len(raw_data_list)):
            char = raw_data_list[end_idx][0]
            typ = raw_data_list[end_idx][1]
            scope = raw_data_list[end_idx][2]
            if typ == 'NUMBER' or typ == 'FLOAT':
                    counter_operand += 1

            elif typ == 'OPERATOR':
                if char == '-' and counter_operand == 1:
                    raw_data_list[end_idx][0] = 'negate'
                elif char == '-' and counter_operand == 2:
                    if prev_scope == scope and raw_data_list[end_idx + 2][0] == 'negate': #If negation operand belongs to current scope
                        raw_data_list[end_idx][0] = 'negate'
                    counter_operand -=  1
                else:
                    counter_operand -=  1
                prev_scope = scope

            end_idx -= 1
        
        # Algorithm for the ^ operator
        idx = 0
        for i in xrange(len(raw_data_list)):
            char = raw_data_list[idx][0]
            typ = raw_data_list[idx][1]
            if char == '^' and typ == 'OPERATOR':
                del raw_data_list[idx]
                first_char = raw_data_list[idx][0]
                first_typ = raw_data_list[idx][1]
                second_char = raw_data_list[idx + 1][0]
                del raw_data_list[idx + 1]
                
                if is_floating_point == False:
                    for j in xrange(int(second_char) - 1):
                        raw_data_list.append(['*', 'OPERATOR'])
                
                    for k in xrange(int(second_char) - 1):
                        raw_data_list.append(['dup', 'OPERATOR'])
            
                elif is_floating_point == True:
                    for h in xrange(int(float(second_char)) - 1):
                        raw_data_list.append(['*', 'OPERATOR'])

                    for g in xrange(int(float(second_char)) - 1):
                        raw_data_list.append(['dup', 'OPERATOR'])

                del raw_data_list[idx]
                raw_data_list.append([first_char, first_typ])
            
            idx += 1

        #Algorithm for the stdout operator
        end_idx = len(raw_data_list) - 1
        for i in xrange(len(raw_data_list)):
            char = raw_data_list[end_idx][0]
            typ = raw_data_list[end_idx][1]
            if char == 'stdout':
                raw_data_list.pop(end_idx)

            elif typ == 'STRING':
                raw_data_list[end_idx][0] = "s\" " + raw_data_list[end_idx][0] + "\" type"

            end_idx -= 1

        return raw_data_list 

    def constant(self, token_list):
        self.token_list = token_list
        raw_data_list = self.remove_brackets()
        postfix_list = []
        is_double_literal = 0
        idx = 0
        is_floating_point = self.check_floating_point(raw_data_list)
        has_specific_operator = self.check_specific_operator(raw_data_list)
        data_list = self.modify_data(raw_data_list, is_floating_point)
        st = s.Stack()
        end_with_string = 0
    
        for i in xrange(len(data_list)):
            char = data_list[idx][0]
            typ = data_list[idx][1]
            end_with_string = 0
            
            if char != "if" and (typ == 'OPERATOR' or typ == 'KEYWORD'):
                is_double_literal = 0
                st.push(char)

            elif typ == "STRING": #stdout string
                end_with_string = 1
                postfix_list.append(char)
           
            elif char != "if" and is_floating_point == False:
                postfix_list.append(char)
                is_double_literal += 1
                
                if is_double_literal == 2:
                    operator_pop = st.pop()
                    
                    if operator_pop == '%':
                        postfix_list.append('mod')
                   
                    elif operator_pop == '!=':
                        postfix_list.append('<>')

                    else:
                        postfix_list.append(operator_pop)
                    
                    is_double_literal = 0
            
                if (idx + 1) == len(data_list):
                    for j in xrange(st.size()):
                        operator_pop = st.pop()
                        
                        if operator_pop == '%':
                            postfix_list.append('mod')
                        
                        elif operator_pop == '!=':
                            postfix_list.append('<>')

                        else:
                            postfix_list.append(operator_pop)
            
            elif char != "if" and  is_floating_point == True:
                if typ == 'FLOAT':
                    postfix_list.append(char + 'e')
                    is_double_literal += 1
                
                else:
                    postfix_list.append(char)
                    is_double_literal += 1

                if is_double_literal == 2:
                    operator_pop = st.pop()

                    if operator_pop == '%':
                        postfix_list.append('mod S>F')
                    
                    elif operator_pop == '!=':
                        postfix_list.append('F<>')

                    else:
                        postfix_list.append('F' + operator_pop)

                    is_double_literal = 0

                if (idx + 1) == len(data_list):
                    for j in xrange(st.size()):
                        operator_pop = st.pop()

                        if operator_pop == '%':
                            postfix_list.append('mod')
                        
                        elif operator_pop == '!=':
                            postfix_list.append('F<>')

                        else:
                            postfix_list.append('F' + operator_pop)

            idx += 1

        #Algorithm for IF statements
        for i in xrange(len(data_list)):
            char = data_list[i][0]
            if char == "if":
                cur_idx = i
                k = 1 # Skip 'if'
                j = 0 # Operator counter
                if raw_data_list[cur_idx + k][1] == 'OPERATOR':
                    k += 1 # skip first operator
                    while raw_data_list[cur_idx + k][1] != 'OPERATOR' and j < 2:
                        j += 1
                        k += 1
                else:
                    k += 1
                postfix_list.insert(cur_idx + k - 1, ": ifftrue IF")
                j = 0 # Operator counter
                if cur_idx + k < len(raw_data_list) and raw_data_list[cur_idx + k][1] == 'OPERATOR':
                    k += 1 # skip first operator
                    while cur_idx + k < len(raw_data_list) and raw_data_list[cur_idx + k][1] != 'OPERATOR' and j < 2:
                        j += 1
                        k += 1
                else:
                    k += 1
                postfix_list.insert(cur_idx + k, ".s")
                if cur_idx + k >= len(raw_data_list) or \
                    raw_data_list[cur_idx + k][3] > raw_data_list[cur_idx + k - 1][3]: # Check if else statement exists within current context
                    postfix_list.insert(cur_idx + k + 1 ,"THEN ;")
                else:
                    postfix_list.insert(cur_idx + k + 1, "ELSE")
                    j = 0 # Operator counter
                    if cur_idx + k < len(raw_data_list) and raw_data_list[cur_idx + k][1] == 'OPERATOR':
                        k += 1 # skip first operator
                        while cur_idx + k < len(raw_data_list) and raw_data_list[cur_idx + k][1] != 'OPERATOR' and j < 2:
                            j += 1
                            k += 1
                    else:
                        k += 1
                    postfix_list.insert(cur_idx + k + 2, ".s THEN ;")

            if end_with_string == True:
                pass

            elif has_specific_operator == True:
                postfix_list.append('. cr')

            elif is_floating_point == True:
                postfix_list.append('F. cr')

            else:
                postfix_list.append('. cr')

            return postfix_list

if __name__ == "__main__":
    print("This is the constant_only.py file")
    print("This is a helper file to the main.py of Milestone #4 for CS 480")
