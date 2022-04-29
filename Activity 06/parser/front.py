# /* Global declarations */
# /* Variables */
charClass = ''
lexeme= []
for i in range(100):
        lexeme.append('')
nextChar=''
lexLen = 0
nextToken = 0
in_fp = ''

#Character classes 
LETTER = 0
DIGIT = 1
UNKNOWN = 99

#Token codes 
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26


# /* lookup - a function to lookup operators and parentheses and return the 
#  * token */
def lookup(ch):
        global nextToken
        if ch == '(':
                addChar()
                nextToken = LEFT_PAREN
        elif ch == ')':
                addChar()
                nextToken = RIGHT_PAREN
        elif ch == '+':
                addChar()
                nextToken = ADD_OP
        elif ch == '-':
                addChar()
                nextToken = SUB_OP
        elif ch == '*':
                addChar()
                nextToken = MULT_OP
        elif ch == '/':
                addChar()
                nextToken = DIV_OP
        else:
                addChar()
                nextToken = ''    
        return nextToken

# /*****************************************************/
# /* addChar - a function to add nextChar to lexeme */
def addChar():
        global lexeme
        global lexLen
        if (lexLen <= 98):
                lexeme[lexLen] = nextChar
                lexLen += 1
                lexeme[lexLen] = ''
                lexLen += 1
        else:
                print("Error - lexeme is too long \n")
 

# /*****************************************************/
# /* getChar - a function to get the next character of input and determine its 
#  * character class */

def getChar():
        global nextChar
        global charClass
        nextChar = in_fp.read(1)

        if (nextChar != ''):
                if (nextChar.isalpha()):
                        charClass = LETTER
                elif (nextChar.isdigit()):
                        charClass = DIGIT
                else:
                        charClass = UNKNOWN
        else:
                charClass = ''

# /*****************************************************/
# /* getNonBlank - a function to call getChar until it returns a non-whitespace 
#  * character */

def getNonBlank():
        global nextChar
        while(nextChar.isspace()):
                getChar()

# /*****************************************************/
# /* lex - a simple lexical analyzer for arithmetic expressions */
def lex():
        global lexLen
        global charClass
        global nextToken
        global lexeme
        lexLen = 0
        getNonBlank()
        # * Parse identifiers */
        if charClass == LETTER:
                addChar()
                getChar()
                while (charClass == LETTER or charClass == DIGIT):
                        addChar()
                        getChar()
                  
                nextToken = IDENT
                

                # /* Parse integer literals */
        elif charClass == DIGIT:
                addChar()
                getChar()
                while (charClass == DIGIT):
                        addChar()
                        getChar()
                nextToken = INT_LIT
                

                # /* Parentheses and operators */
        elif charClass == UNKNOWN:
                lookup(nextChar)
                getChar()
                

        elif charClass == '':
                nextToken = ''
                lexeme[0] = 'E'
                lexeme[1] = 'O'
                lexeme[2] = 'F'

        lexeme = list(map(str,lexeme))
        print("Next token is: {}, Next lexeme is {}\n".format(nextToken,''.join(lexeme)))       
        return nextToken
#/* End of function lex */


#******************************************************/
#/* main driver */

try:
        in_fp = open("front.in", "r") 
        getChar()
        lex()
        while (nextToken != ''):
                lex()
except:
        print("ERROR - cannot open front.in \n")
                                

#/*****************************************************/
