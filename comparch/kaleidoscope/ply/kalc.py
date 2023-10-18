#!/usr/bin/env python

import sys
sys.path.insert(0, "../..")

#if sys.version_info[0] >= 3:
#    raw_input = input

import ply.lex as lex
import ply.yacc as yacc
import os


class Parser:
    """
    Base class for a lexer/parser that has the rules defined as methods
    """
    tokens = ()
    precedence = ()
    reserved = ()

    def __init__(self, **kw):
        self.debug = kw.get('debug', 0)
        self.names = {}
        try:
            modname = os.path.split(os.path.splitext(__file__)[0])[
                1] + "_" + self.__class__.__name__
        except:
            modname = "parser" + "_" + self.__class__.__name__
        self.debugfile = modname + ".dbg"
        self.tabmodule = modname + "_" + "parsetab"
        # print self.debugfile, self.tabmodule

        # Build the lexer and parser
        lex.lex(module=self, debug=self.debug)
        yacc.yacc(module=self,
                  debug=self.debug,
                  debugfile=self.debugfile,
                  tabmodule=self.tabmodule)

    def run(self, sourceFile, targetFile):
        with open(sourceFile, 'r') as sc:
            scode = sc.read()
            yacc.parse(scode)

class Calc(Parser):
    
    reserved = { 'def': 'DEF',
                 'if': 'IF',
                 'else': 'ELSE',
                 'true': 'TRUE',
                 'false': 'FALSE'
                }

    tokens = list(reserved.values()) + [
        # Integers and identifiers
        'INT', 'ID',
        # Boolean operations
        'LT', 'GT', 'LEQ', 'GEQ', 'EQ', 'NEQ', 
        # Arithmetic operations
        'ADD', 'SUB', 'MUL', 'DIV', 'MOD',
        # Delimiters
        'LCURBRACE', 'RCURBRACE', 'LPAREN', 'RPAREN', 'COMMA'
    ]

    # Tokens
    t_INT   = r'[0-9]+'
    t_LT    = r'<'
    t_GT    = r'>'
    t_LEQ   = r'<='
    t_GEQ   = r'>='
    t_EQ    = r'=='
    t_NEQ   = r'!='
    t_ADD   = r'\+'
    t_SUB   = r'-'
    t_MUL   = r'\*'
    t_DIV   = r'/'
    t_MOD   = r'%'  

    t_LCURBRACE = r'{'
    t_RCURBRACE = r'}'
    t_LPAREN    = r'\('
    t_RPAREN    = r'\)'
    t_COMMA    = r','

    t_ignore = " \t\r"

    def  t_ID(self,t):
        r'[a-z]+'
        t.type = self.reserved.get(t.value, 'ID')
        return t

    def t_COMMENT(self, t):
        r'(/\*(.|\n)*?\*/)'
        # No return value, token discarded
        pass

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        print("Ilegal character \"{}\" at line {}".format(t.value[0], t.lexer.lineno))
        t.lexer.skip(1)

    # Parsing rules

    def p_program(self, p):
        """
         program : functionDefList expression
        """
        pass

    def p_functionDef(self, p):
        """
         functionDef : DEF ID LPAREN idList RPAREN LCURBRACE expression RCURBRACE
        """
        pass

    ##
    # Parse a  list of function definitions.
    # 
    # The list might be empty or contain more than one definition.
    ##
    
    # A list of function definitions might be empty
    def p_functionDefList_1(self, p):
        """
         functionDefList : 
        """
        pass

    def p_functionDefList_2(self, p):
        """
         functionDefList : functionDef
        """
        pass

    def p_functionDefList_3(self, p):
        """
         functionDefList : functionDefList functionDef
        """
        pass

    ##
    # Parse a list of identifiers
    ##
    def p_idList_1(self, p):
        """
         idList : ID
        """
        pass

    def p_idList_2(self, p):
        """
         idList : 
        """
        pass

    def p_idList_3(self, p):
        """
         idList : idList COMMA ID
        """
        pass

    precedence = (
        ('left', 'ADD', 'SUB'),
        ('left', 'MUL', 'DIV', 'MOD'),
    )

    def p_expression(self, p):
        """
         expression : LPAREN expression RPAREN
                    | IF LPAREN logicalExpression RPAREN LCURBRACE expression RCURBRACE ELSE LCURBRACE expression RCURBRACE
                    | ID LPAREN expressionList RPAREN
                    | expression MUL expression
                    | expression DIV expression
                    | expression MOD expression
                    | expression ADD expression
                    | expression SUB expression
                    | INT
                    | ID
         """
        pass

    def p_expressionList_1(self, p):
        """
            expressionList : expression
        """    
        pass

    def p_expressionList_2(self, p):
        """
            expressionList : expressionList COMMA expression
        """    
        pass

    def p_logicalExpression(self, p):
        """
         logicalExpression : expression LT expression
                           | expression GT expression
                           | expression LEQ expression
                           | expression GEQ expression
                           | expression EQ expression
                           | expression NEQ expression
                           | TRUE
                           | FALSE
         """
        pass

    def p_error(self, p):
        if p:
            print("Syntax error at '%s'" % p.value)
        else:
            print("Syntax error at EOF")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Example call: {} input.kl output.asm".format(sys.argv[0]))
    else:
        sourceFile = sys.argv[1]
        targetFile = sys.argv[2]
        calc = Calc()
        calc.run(sourceFile, targetFile)