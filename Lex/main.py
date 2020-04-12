import parser_my
import time
import os.path

def PLYConsolecheck(_str):
    _parser = parser_my.Parser()
    _str += '\n'
    _res = _parser.PLYCheck(_str)
    if _parser.flag:
        return _str.rstrip('\n') + ' --- Correct\n'
    else:
        return _str.rstrip('\n') + ' --- Incorrect\n'


a = str(input())
print(PLYConsolecheck(a))
