import re
import ply.lex as lex

class Lexer:
    tokens = (
        'GRID', 'CMD1', 'CMD2', 'CMD3', 'SP', 'MACROS', 'OPERANDS', 'NL', 'UNKNOWN'
    )

    #t_GRID = r'\#'
    #t_CMD = r'add|chk|def|und'
    #t_MACROS = r'[A-Z]){1,10}'
    def __init__(self):
        self.lexer = lex.lex(module=self)

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def t_GRID(self, t):
        r'\#'
        if t.lexer.current_state() == 'INITIAL':
            print('INITIAL')
            #t.lexer.begin('CMD')
        else:
            t.lexer.begin('INITIAL')
        return t

    def t_CMD1(self, t):
        r'(add|def)\s'
        #t.lexer.begin('NL')
        return t

    def t_CMD2(self,t):
        r'(chk)\s'
        return t

    def t_CMD3(self,t):
        r'(und)\s'
        return t

    def t_SP(self, t):
        r'\s'
        #t.lexer.begin('MACROS')
        return t

    def t_NL(self, t):
        r'\n'
        return t

    def t_MACROS(self, t):
        r'([A-Z]){1,10}'
        #t.lexer.begin('NL2')
        return t

    def t_OPERANDS(self, t):
        r'(((\b[^\s\,\\\t\#]+\b)\s)*)(\b[^\s\,\\\t\#]+\b)'
        return t

    def t_ANY_UNKNOWN(self, t):
        r'(.)+'
        t.lexer.begin('INITIAL')
        return t

    def t_ANY_error(self, t):
        t.lexer.skip(1)
        t.lexer.begin('INITIAL')
        return t

# l = Lexer()
# l.input('#und HJAHH')
# while True:
#     tok = l.token()
#     if not tok:
#         break
#     print(tok)