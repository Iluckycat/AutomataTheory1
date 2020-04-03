import re
import ply.lex as lex

class Lexer:
    tokens = (
        'CMD', 'GRID', 'MACROS', 'OPERAND', 'NL', 'UNKNOWN'
    )

    #t_GRID = r'#'
    #t_CMD = r'add|chk|def|und'
    #t_MACROS = r'[A-Z]){1,10}'
    def __init__(self):
        self.lexer = lex.lex(module=self)

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def t_GRID(self, t):
        r'#'
        if t.lexer.current_state() == 'INITIAL':
            t.lexer.begin('cmd')
        else:
            t.lexer.begin('INITIAL')
        return t

    def t_CMD(self, t):
        r'\s(add|chk|def|und)\s'