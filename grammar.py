from lexer import *
import math

# Parsing rules

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}


def p_statement_assign(p):
    'statement : NAME EQUALS expression'
    names[p[1]] = p[3]


def p_statement_expr(p):
    'statement : expression'
    print(p[1])


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MINOR expression
                  | expression MINOR EQUALS expression
                  | expression MAJOR expression
                  | expression MAJOR EQUALS expression
                  | expression EQUALS EQUALS expression
                  | expression EXP expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '<' and p[3] != '=':
        p[0] = p[1] < p[3]
    elif p[2] == '<' and p[3] == '=':
        p[0] = p[1] <= p[4]
    elif p[2] == '>' and p[3] != '=':
        p[0] = p[1] > p[3]
    elif p[2] == '>' and p[3] == '=':
        p[0] = p[1] >= p[4]
    elif p[2] == '=' and p[3] == '=':
        p[0] = p[1] == p[4]
    elif p[2] == '**':
        p[0] = p[1] ** p[3]


def p_expression_uminus(p):
    "expression : MINUS expression %prec UMINUS"
    p[0] = -p[2]


def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]


def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_expression_pow(p):
    "expression : POW LPAREN expression COMMA expression RPAREN"
    p[0] = p[3] ** p[5]


def p_expression_sqrt(p):
    "expression : SQRT LPAREN expression RPAREN"
    p[0] = math.sqrt(p[3])


def p_expression_myrna(p):
    "expression : MYRNA LPAREN expression RPAREN"
    p[0] = "Myrna deu nota 10 para esse trabalho e mandou " + str(p[3]) + " emoticons no teams"


def p_expression_bhaskara(p):
    "expression : BHASKARA LPAREN expression COMMA expression COMMA expression RPAREN"
    delta = (p[5] * p[5]) - (4 * p[3] * p[7])
    pos_tmp = ((p[5] * (-1)) + math.sqrt(delta))/(2 * p[3])
    neg_tmp = ((p[5] * (-1)) - math.sqrt(delta))/(2 * p[3])
    p[0] = "x = +" + str(pos_tmp) + " ou " + str(neg_tmp)


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
