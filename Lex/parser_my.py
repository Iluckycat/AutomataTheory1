import lexer
import ply.yacc as yacc


class Parser:
    tokens = lexer.Lexer.tokens

    def __init__(self):
        self._lexer = lexer.Lexer()
        self._parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        self._stats = {}
        self.flag = False

    def p_temp(self, p):
        """temp : GRID CMD1 SP MACROS SP OPERANDS
            | GRID CMD2 SP MACROS SP OPERANDS NL
            | GRID CMD2 SP MACROS NL
            | GRID CMD3 SP MACROS """
        if len(p) == 5:
            print('CMD3\n')
            p[0] = p[1] + p[2] + p[3] + p[4]
            # if p[2] != 'und':
            #     self.flag = False
            # else:
            self.flag = True
        elif len(p) == 6:
            print('CMD2\n')
            print('NONE OPERANDS\n')
            p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
            # if p[2] != 'chk':
            #     self.flag = False
            # else:
            self.flag = True
        elif len(p) == 7:
            print('CMD1\n')
            p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
            # if p[2] != ('add|def'):
            #     self.flag = False
            # else:
            self.flag = True
        elif len(p) == 8:
            print('CMD2\n')
            print('IS OPERANDS\n')
            p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
            # if p[2] != 'chk':
            #     self.flag = False
            # else:
            self.flag = True

    def p_temp_zero_error(self, p):
        """temp : err NL"""
        p[0] = p[1] + p[2]

    def p_temp_first_error(self, p):
        """temp : GRID err NL"""
        p[0] = p[1] + p[2] + p[3]

    def p_temp_second_error(self, p):
        """temp : GRID CMD1  err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_temp_third_error(self, p):
        """temp : GRID CMD1 SP err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    def p_temp_fourth_error(self, p):
        """temp : GRID CMD1 SP MACROS err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

    def p_temp_fivth_error(self, p):
        """temp : GRID CMD1 SP MACROS SP err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] +p[7]

    def p_err(self, p):
        """err : UNKNOWN"""
        p[0] = p[1]
    def p_error(self,p):
        pass

    def PLYCheck(self, _str, _file=False):
        if _file == False:
            self._stats.clear()
        self.flag = False
        _res = self._parser.parse(_str)
        return _str


y = Parser()
y.PLYCheck('#und HJAHH sdsdsds ddsd')
print(y.flag)
