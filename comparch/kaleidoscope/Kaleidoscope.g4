// Defines a grammar for the Kaleidoscope language
grammar Kaleidoscope;

program  : functionDef* entry=expression;

// Functions
functionDef:  DEF name=ID '(' (ID (',' ID)*)*  ')' '{' body=expression '}';

// Expression
expression	
	: '(' exp=expression ')'									        				        #parenExpr
	| IF '(' gExp=logicalExpression ')' '{' tExp=expression '}' ELSE '{' eExp=expression '}'	#condExpr
	| name=ID '(' (expression (',' expression)*)* ')' 								            #callExpr
	| left=expression op=(MUL | DIV | MOD) right=expression						                #multDivExpr
	| left=expression op=(ADD | SUB) right=expression							                #addSubExpr
	| INT 																		                #constExpr
	| ID 																		                #variableExpr
	;

logicalExpression
	: left=expression op=(LT | GT | LEQ | GEQ | EQ | NEQ) right=expression            #opLExpr
	| TRUE                                                                            #lTrue
	| FALSE                                                                           #lFalse
	;

/**
 * Lexer rules
 *
 * Here we define the tokens identified by the lexer.
 */

// Comments
OPEN_COMMENT :  '/*';
CLOSE_COMMENT :  '*/';
COMMENT : OPEN_COMMENT .*? CLOSE_COMMENT -> channel(HIDDEN);

// Keywords
DEF   : 'def';
IF    : 'if';
ELSE  : 'else';
TRUE  : 'true';
FALSE : 'false';

// Arithmetic operations
ADD  :  '+';
SUB  :  '-';
MUL  :  '*';
DIV  :  '/';
MOD  :  '%';

// Boolean operations
LT  :  '<';
GT  :  '>';
LEQ :  '<=';
GEQ :  '>=';
EQ  :  '==';
NEQ  : '!=';

// Integers and identifiers
INT  :  [0-9]+;
ID   :  [a-z]+ ;

// Ignore white space, tab and new lines.
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
