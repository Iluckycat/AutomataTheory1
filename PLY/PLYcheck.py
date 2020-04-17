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

def PLYfilecheck():
    _parser = parser_my.Parser()
    inf = open('../StringAnalyzer/Files/string.txt', 'r')
    ouf = open('../StringAnalyzer/Files/PLYOutput', 'w')
    _starttime = time.time()
    for line in inf.readlines():
        _res = _parser.PLYCheck(line, _file=True)
        if _parser.flag:
            ouf.write(line.rstrip('\n') + ' --- Correct\n')
        else:
            ouf.write(line.rstrip('\n') + ' --- Incorrect\n')
    _endtime = time.time()

    ouf.write('\n')
    ouf.write('---------------------------------- SOME STATS ---------------------------------- \n')
    ouf.write('\n')
    ouf.write('Total number of match is ' + str(_parser.totalmatch) + '\n')
    print('Total number of match is ' + str(_parser.totalmatch) + '\n')
    for key, value in _parser._stats.items():
        ouf.write('\t' + 'Macro ' + key + ' checked ' + str(value) + ' times;' + '\n')

    if os.path.isfile('../StringAnalyzer/Files/time.txt'):
        timefile = open('../StringAnalyzer/Files/time.txt', 'a')
        timefile.write('Analyzing with PLY completed in ' + str(_endtime - _starttime) + ' seconds\n')
    else:
        timefile = open('../StringAnalyzer/Files/time.txt', 'w')
        timefile.write('Analyzing with PLY completed in ' + str(_endtime - _starttime) + ' seconds\n')
    timefile.close()
    print('Analyzing with PLY completed in', _endtime - _starttime, 'seconds')
    inf.close()
    ouf.close()


#a = str(input())
#print(PLYConsolecheck(a))
#PLYfilecheck()
