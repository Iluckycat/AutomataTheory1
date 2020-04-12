import lexer
import ply.yacc as yacc


class Parser:
    tokens = lexer.Lexer.tokens

    def __init__(self):
        self._lexer = lexer.Lexer()
        self._parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        self._stats = {}
        self.flag = False

    def p_array(self, p):
        """array : GRID CMD1 SP MACROS SP OPERANDS
            | GRID CMD2 SP MACROS SP OPERANDS NL
            | GRID CMD2 SP MACROS NL
            | GRID CMD3 SP MACROS """
        if len(p) == 4:
            print('CMD3\n')
            p[0] = p[1] + p[2] + p[3] + p[4]
            self.flag = True
        elif CMD2 is not None :
            print('CMD2\n')
            if OPERANDS is not None:
                print('OPERANDS\n')
                p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
                self.flag = True
            else:
                print('NONE OPERANDS\n')
                p[0] = p[1] + p[2] + p[3] + p[4]
                self.flag = True
        elif CMD1 is not None:
            print('CMD1\n')
            p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
            self.flag = True

    def p_array_zero_error(self, p):
        """array : err NL"""
        p[0] = p[1] + p[2]

    def p_array_first_error(self, p):
        """array : GRID err NL"""
        p[0] = p[1] + p[2] + p[3]

    def p_array_second_error(self, p):
        """array : GRID CMD1  err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_array_third_error(self, p):
        """array : GRID CMD1 SP err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    def p_array_fourth_error(self, p):
        """array : GRID CMD1 SP MACROS err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

    def p_array_fivth_error(self, p):
        """array : GRID CMD1 SP MACROS SP err NL"""
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
        print(_res)
        return _str


y = Parser()
y.PLYCheck('#und JHSJH')
print(y.flag)
