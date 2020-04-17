import lexer
import ply.yacc as yacc


class Parser:
    tokens = lexer.Lexer.tokens

    def __init__(self):
        self._lexer = lexer.Lexer()
        self._parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        self._stats = {}
        self.totalmatch = 0
        self.flag = False
        self._macros = ''

    def p_temp(self, p):
        """temp : GRID CMD1 SP MACROS SP OPERANDS NL
            | GRID CMD2 SP MACROS SP OPERANDS NL
            | GRID CMD2 SP MACROS NL
            | GRID CMD3 SP MACROS NL"""

        # for i in range(len(p)):
        #     print(i, ' - ',p[i])

        if len(p) == 8:
            if (p[2] == 'add') or (p[2] == 'def'):
                # print('CMD is add or def\n')
                self.flag = True
                self.totalmatch += 1
                p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

            if p[2] == 'chk':
                # print('CMD is chk with operands\n')
                self.flag = True
                p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
                self.totalmatch += 1
                _macros = p[4]
                if _macros is not None:
                    if self._stats.get(_macros) is not None:
                        self._stats[_macros] += 1
                    else:
                        self._stats[_macros] = 1

        elif len(p) == 6:
            if p[2] == 'chk':
                # print('CMD is chk without operands\n')
                self.flag = True

                p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
                self.totalmatch += 1
                _macros = p[4]
                if _macros is not None:
                    if self._stats.get(_macros) is not None:
                        self._stats[_macros] += 1
                    else:
                        self._stats[_macros] = 1

            if p[2] == 'und':
                # print('CMD is und')
                self.flag = True
                self.totalmatch += 1
                p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

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
        if len(_str) < 81:
            _res = self._parser.parse(_str)
        #     print(_res)
        # print(self.flag)
        return _str


# y = Parser()
# s = '#def ZA yw HLuwHBXmsPQqbsY CWDuwHBXmsPQqbsY CWD\n'
# y.PLYCheck(s)
