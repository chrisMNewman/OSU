\ CS 480 - Milestone #1
\ Name:     Sang Shin
\ Due Date: 01/15/2014

\ 1. Print "Hello World\n"
." EXERCISE 1" cr
." printf('Hello World'\n);" cr
." Hello, World" cr
cr

\ 2. Bonus 5 pts: print only a certain number of characters from the string 
." EXERCISE 2" cr
." Print only a certain number of characters from the string" cr
cr
\ 3. 16 / 32 + 74 * 16^3 + 5 % 10 = 303109
." EXERCISE 3" cr
." 16 / 32 + 74 * 16^3 + 5 % 10" cr
16 32 / 74 16 dup dup * * * 5 10 mod + + . cr
cr

\ 4. 16.0 / 32.0 + 74.0 * 16.0^3.0 + 5 % 10 = 303109.5
." EXERCISE 4" cr
." 16.0 / 32.0 + 74.0 * 16.0^3.0 + 5 % 10" cr
16.0e 32.0e F/ 74.0e 16.0e fdup fdup F* F* F* 5 10 mod S>D D>F F+ F+ F. cr
cr

\ 5. 16.0e0 / 32.0e0 + 74.0e0 * 16.0e0 ^ 3.0e0 + 5 % 10 = 303109.5
." EXERCISE 5" cr 
." 16.0e0 / 32.0e0 + 74.0e0 * 16.0e0^3.0e0 + 5 % 10" cr
16.0e0 32.0e0 F/ 74.0e0 16.0e0 fdup fdup F* F* F* 5 10 mod S>D D>F F+ F+ F. cr
cr

\ 6. 16 / 32.0 + 74.0 * 16^3 + 5 % 10 = 303109.5
." EXERCISE 6" cr 
." 16 / 32.0 + 74.0 * 16^3 + 5 % 10" cr
16 S>D D>F 32.0e F/ 74.0e 16 dup dup * * S>D D>F F* 5 10 mod S>D D>F F+ F+ F. cr
cr

\ 7. y = 16; x = 32.0e0; y + x - 3.0e0 * 6 / 10.0 = 46.2
." EXERCISE 7" cr
." y = 16; x = 32.0e0; y + x - 3.0e0 * 6 / 10.0" cr
Variable y
Variable x
16 y !
32.0e0 x F!
y @ S>D D>F x F@ 3.0e0 6 S>D D>F 10.0e F/ F* F- F+ F. cr
cr

\ 8. if 5 < 3 then 7 else 2
." EXERCISE 8" cr
." if 5 < 3 then 7 else 2" cr
: ?LESSTHAN
    5 3 < IF
    2 ELSE
    7 THEN 
;

?LESSTHAN . cr
cr

\ 9. if 5 > 3 then 7 else 2
." EXERCISE 9" cr
." if 5 > 3 then 7 else 2" cr
: ?GREATERTHAN
    5 3 > IF
    2 ELSE
    7 THEN
;

?GREATERTHAN . cr
cr

\ 10. for ( i = 0; i <= 5; i++ ) { printf("%d", i); }
." EXERCISE 10" cr
."  for ( i = 0; i <= 5; i++ )" cr
."  {" cr
."      printf('%d', i);" cr
."  }" cr
: ?FORLOOP 
    6 0 DO I . cr LOOP 
;

?FORLOOP
cr

\ 11. double convertint (int x) { return ((double)x); }
." EXERCISE 11" cr
."  double convertint (int x)" cr
."  {" cr
."      return ((double)x);" cr
."  }" cr
: ?CONVERTINT
    dup S>D D>F
;
." Convert 100 to floating point" cr
100 ?CONVERTINT F. cr

cr ." Convert 200 to floating point" cr
200 ?CONVERTINT F. cr
cr

\ 12. int fact (int i) { if (i <= 0) return 1; else return i*fact(i-1);}
." EXERCISE 12" cr
."  int fact (int i)" cr
."  {" cr
."      if ( i <= 0 )" cr
."          return 1;" cr
."      else" cr
."          return i * fact(i-1);" cr
."  }" cr
: ?FAC ( n -- n )
    \ Reference: progopedia.com/implementation/gforth
    dup 1 > IF
        dup 1 - recurse *
    else
        drop 1
    endif
;

." Test Factorial Function with 0" cr
0 ?FAC . cr

cr ." General Factorial Function Test" cr
5 ?FAC . cr
10 ?FAC . cr
cr

\ 13. int fib (int i) { if (i==0) return 0; else if (i==1) return 1; else return fib(i-1)+fib(i-2) }
." EXERCISE 13" cr
."  int fib (int i)" cr
."  {" cr
."      if ( i == 0 )" cr
."          return 0;" cr
."      else if ( i == 1 )" cr
."          return 1;" cr
."      else" cr
."          return fib(i-1) + fib(i-2);" cr
."  }" cr
: ?FIB ( n -- f)
    \ Duplicate the top of the stack and check is it is less and 2
    \ Decrement the top of the stack number and duplicate it
    \ Recurse the function and swap the two numbers on the top of the stack
    \ Decrement the top of the stack number and recurse
    \ Add the two numbers on the top of the stack
    \ Reference: progopedia.com/implementation/gforth
    dup 2 u< if exit then
    1- dup recurse swap 1- recurse + 
;

: ?MAIN
    \ This main function is to test the fib function above
    \ It is to test the fib function by performing a loop
    0 do
        i over execute . cr
    loop drop
;

\ Test the fibonacci number function by printing the 9th fib number
." Print the 9th Fibonacci Number" cr
9 ?FIB . cr

\ Test the fibonacci number function by printing the first 10 numbers
cr ." Print the first 10 Fibonacci Numbers" cr
' ?FIB 10 ?MAIN cr







bye
