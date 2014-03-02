# -----------------------------------------------
# file          : main.py
# author        : Sang Shin | Chris Newman
# date          : 02-20-2014
# class         : CS 480 | Milestone #4
# description   : Primary execution file
# -----------------------------------------------
#!/usr/bin/python
import sys
import lexical_analyzer as lx
import token_parser as pr
import constant_only as co

character_buffer = []

def initialize(filename):
    ''' Initialize by reading in the file and splitting all strings into characters '''
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                for character in line:
                    character_buffer.append(character)

    except IOError:
        print("Could not read file:", filename)
        sys.exit()

def print_token_file(filename, token_table):
    ''' Print the token table to a file '''
    with open(filename + '.out', 'a') as f:
        for token in token_table:
            f.write("%s\n" % token)
    
def print_parser_file(filename, result):
    ''' Print the information output by Parser '''
    with open("stutest.out", 'a') as f:
        f.write("=============== %s ===============\n" % filename)
        if filename == "ctest1" or filename == "ctest2" or filename == "ctest3":
            f.write("CTEST RESULT:\t%s\n" % result)
        
        else:
            f.write("PTEST RESULT:\t%s\n" % result)
        
        f.write("\n")

def print_postfix_file(filename, token_table, postfix_list):
    ''' Print the postfix to a file '''
    idx = 0
    with open("stutest.out", 'a') as f:
        f.write("=============== %s ===============\n" % filename)
        for i in xrange(len(token_table)):
            token = token_table[idx][0]
            f.write("%s " % token)
            idx += 1
        
        f.write("\n")
        for postfix in postfix_list:
            f.write("%s " % postfix)
        
        f.write("\n\n")
    f.close()

    with open(filename + ".fs", 'a') as f:
        for postfix in postfix_list:
            f.write("%s " % postfix)
    
    f.close()

def print_file(FILE_NAME, token_table):
    ''' Print the token table to a file '''
    with open(FILE_NAME + '_out', 'a') as f:
        for token in token_table:
            f.write("%s\n" % token)

    print("%s_out file was created" % FILE_NAME)
    
def main():
    TEST_FILE = sys.argv[1]
    initialize(TEST_FILE)
    token_table = lx.Lexer().tokenize(character_buffer)
    #print_file("result", token_table)
    result = pr.Parser().parse(token_table)
    postfix_list = co.Constant_Only().constant(token_table)
    print_postfix_file(TEST_FILE, token_table, postfix_list)
    print_parser_file(TEST_FILE, result)

if __name__ == '__main__':
    main()
