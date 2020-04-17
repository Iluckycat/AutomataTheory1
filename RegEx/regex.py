import re
import time
import string
import os.path


def regexchkfile():
    _myfille = '../StringAnalyzer/Files/string.txt'
    _result_file = '../StringAnalyzer/Files/RegExOutput.txt'

    _inp_file = open(_myfille, mode='r', encoding='Latin-1')
    _out_file = open(_result_file, mode='w', encoding='Latin-1')

    _regEx = r'^(((\#)((((def|add)(\s)(([A-Z]){1,10})(\s)(((\b[^\s\,\\\t\#]+\b)\s)*)(\b[^\s\,\\\t\#]+\b)(\n))'
    _regEx += r'|((chk)(\s)(([A-Z]){1,10})(\s?)(((\b[^\s\,\\\t\#]+\b)\s?)*)(\b[^\s\,\\\t\#]+\b)?)'
    _regEx += r'|((und)(\s)(([A-Z]){1,10})(\n))))))$'
    _total = 0
    _total_chk = 0
    _total_und = 0
    _total_add_def = 0

    stat = {}
    tm = time.time()
    _out_file.write('ALL MATCHES: '+'\n')
    _out_file.write('-------------------------------------------------------------------------------------------------------------'+'\n\n')
    for line in _inp_file:
        _result = re.fullmatch(_regEx, line)
        if _result is not None:
            _total += 1
            if len(_result.group(2)) < 81:
                if _result.group(17) is not None:
                    _total_chk += 1
                    _out_file.write('\t'+_result.group(3)+_result.group(17))
                    # print(_result.group(17))
                    tmp = _result.group(20)
                    if stat.get(tmp) is not None:
                        stat[tmp] += 1
                    else:
                        stat[tmp] = 1

                if _result.group(27) is not None:
                    _total_und += 1
                    _out_file.write('\t'+_result.group(3)+_result.group(27)+'\n')
                    #print(_result.group(27))
                if _result.group(6) is not None:
                    _total_add_def += 1
                    _out_file.write('\t'+_result.group(3)+_result.group(6)+'\n')
                    #print(_result.group(6))
            else:
                _total -= 1

    if os.path.isfile('../StringAnalyzer/Files/time.txt'):
        timefile = open('../StringAnalyzer/Files/time.txt', 'a')
        timefile.write('Analyzing with RegEx completed in ' + str(time.time()-tm) + ' seconds\n')
    else:
        timefile = open('../StringAnalyzer/Files/time.txt', 'w')
        timefile.write('Analyzing with SMC completed in ' + str(time.time()-tm) + ' seconds\n')
        print('Analyzing with RegEx completed in ' + str(time.time()-tm) + ' seconds\n')
    timefile.close()

    _out_file.write('\n'+'-------------------------------------------------------------------------------------------------------------'+'\n')
    _out_file.write('Timing'+'\n')
    _out_file.write('-------------------------------------------------------------------------------------------------------------'+'\n\n')
    _out_file.write('\t'+'Program worked:' + str(time.time()-tm)+' sec'+'\n')

    _out_file.write('\n'+'-------------------------------------------------------------------------------------------------------------'+'\n')
    _out_file.write('Some information about matches'+'\n')
    _out_file.write('-------------------------------------------------------------------------------------------------------------'+'\n\n')
    _out_file.write('\t'+'Total match: '+str(_total)+'\n')
    print('\t'+'Total match: '+str(_total)+'\n')
    _out_file.write('\t'+'Total match chk: '+str(_total_chk)+'\n')
    _out_file.write('\t'+'Total match und: '+str(_total_und)+'\n')
    _out_file.write('\t'+'Total match add and def: '+str(_total_add_def)+'\n')

    _out_file.write('\n'+'-------------------------------------------------------------------------------------------------------------'+'\n')
    _out_file.write('Some stats'+'\n')
    _out_file.write('-------------------------------------------------------------------------------------------------------------'+'\n\n')
    for key, value in stat.items():
        _out_file.write('\t'+'Macro ' + key + ' checked ' + str(value) + ' times;' + '\n')




