import re
import ply.lex as lex


class Lexer:

    tokens = (
        'GRID', 'CMD1', 'CMD2', 'CMD3', 'SP', 'MACROS', 'OPERANDS', 'NL', 'UNKNOWN'
    )

    states = (
        ('operands', 'exclusive'),
    )

    t_ANY_ignore = ''

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def t_GRID(self, t):
        r'\#'
        return t

    def t_CMD1(self,t):
        r'(add|def)'
        return t

    def t_CMD2(self,t):
        r'(chk)'
        return t

    def t_CMD3(self,t):
        r'(und)'
        return t

    def t_ANY_NL(self,t):
        r'\n'
        t.lexer.begin('INITIAL')
        return t

    def t_ANY_SP(self,t):
        r'\s'
        return t


    def t_MACROS(self,t):
        r'([A-Z]){1,10}'
        t.lexer.begin('operands')
        return t

    def t_operands_OPERANDS(self,t):
        r'(((\b[^\s\,\\\t\#]+\b)\s)*)(\b[^\s\,\\\t\#]+\b)'
        return t

    def t_ANY_UNKNOWN(self,t):
        r'(.)+'
        t.lexer.begin('INITIAL')
        return t

    def t_ANY_error(self,t):
        t.lexer.skip(1)
        t.lexer.begin('INITIAL')
        return t


# l = Lexer()
# l.input('#def ZA yw HLuwHBXmsPQqbsY CWDuwHBXmsPQqbsY CWD\n')
# while True:
#     tok = l.token()
#     if not tok:
#         break
#     print(tok)
