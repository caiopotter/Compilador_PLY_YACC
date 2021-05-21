import sys
sys.path.insert(0, "../..")

reserved = {
    'pow': 'POW',
    'sqrt': 'SQRT',
    'myrna': 'MYRNA',
    'bhaskara': 'BHASKARA'
}

tokens = [
    'NAME', 'NUMBER',
    'PLUS', 'MINUS', 'EXP', 'TIMES', 'DIVIDE', 'EQUALS',
    'LPAREN', 'RPAREN', 'MINOR', 'MAJOR', 'COMMA'
] + list(reserved.values())

# literals = ['=', '+', '-', '*', '/', '(', ')', ',', '>', '<', '>', '<']

# Tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_EXP = r'\*\*'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MINOR = r'\<'
t_MAJOR = r'\>'
t_COMMA = r'\,'

#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:  # Check for reserved words
        t.type = reserved[t.value]
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()
