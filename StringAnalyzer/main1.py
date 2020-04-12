import sys
sys.path.insert(0, '../SMC')
import SMCCheck
import time
import os.path

def SMCfilecheck():
    statemachine = AutomataAnalyzer.AutomataAnalyzer()
    inf = open('../StringAnalyzer/Files/string.txt', 'r')
    ouf = open('../StringAnalyzer/Files/SMCOut.txt', 'w')
    total_num_match = 0
    stat = {}
    statemachine.Check('gg')

    _starttime = time.time()
    for line in inf.readlines():
        match = statemachine.Check(line)
        if match:
            ouf.write(line.rstrip('\n') + ' --- Correct\n')
            total_num_match += 1
            if statemachine.GetCmd() == 'chk':
                tmp = statemachine.GetMacros()
                if tmp is not None:
                    if stat.get(tmp) is not None:
                        stat[tmp] += 1
                    else:
                        stat[tmp] = 1
        else:
            ouf.write(line.rstrip('\n') + ' --- Incorrect\n')
    ouf.write('\n')
    ouf.write('---------------------------------- SOME STATS ---------------------------------- \n')
    ouf.write('\n')
    ouf.write('Total number of match is ' + str(total_num_match)+'\n')
    for key, value in stat.items():
        ouf.write('\t'+'Macro ' + key + ' checked ' + str(value) + ' times;' + '\n')
    _endtime = time.time()
    if os.path.isfile('../StringAnalyzer/Files/time.txt'):
        timefile = open('../StringAnalyzer/Files/time.txt', 'a')
        timefile.write('Analyzing with SMC completed in ' + str(_endtime - _starttime) + ' seconds\n')
    else:
        timefile = open('../StringAnalyzer/Files/time.txt', 'w')
        timefile.write('Analyzing with SMC completed in ' + str(_endtime - _starttime) + ' seconds\n')
    timefile.close()
    print('Analyzing with SMC completed in ' + str(_endtime - _starttime) + ' seconds\n')
    print(str(total_num_match))
    inf.close()
    ouf.close()


SMCfilecheck()
