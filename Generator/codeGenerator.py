import random
import string
import time


def makerndstr(size):
    return ''.join(random.choice(string.ascii_letters) for i in range(size))


def makerndstrsp(size):
    return ''.join(random.choice(string.ascii_letters + ' ') for i in range(size))


def makerndupstr(size):
    return ''.join(random.choice(string.ascii_uppercase) for i in range(size))


def makefile(_num):
    _commands = ['add', 'def', 'chk', 'und']
    with open('../StringAnalyzer/Files/string.txt', 'w') as ouf:
        tm = time.time()
        for i in range(_num):
            bufstr = ''
            if random.randint(1, 4) > 1:
                bufstr += '#'
            if random.randint(1, 20) > 19:
                bufstr += makerndstr(random.randint(0, 5))
            _command = random.choice(_commands)
            _command += makerndstr(random.randint(0, 1))
            bufstr += _command
            bufstr += ' '
            if random.randint(1, 20) > 19:
                bufstr += makerndupstr(random.randint(0, 5))
            _macros = random.choice(string.ascii_uppercase)
            _macros += makerndupstr(random.randint(0, 5))
            bufstr += _macros
            if random.randint(1, 20) > 6:
                bufstr += ' '
                bufstr += makerndstrsp(random.randint(0, 5))
                _inp = random.choice(string.ascii_letters + ' ')
                _inp += makerndstrsp(random.randint(0, 30))
                _inp += makerndstr(random.randint(0, 1))
                bufstr += _inp
            else:
                _inp = ''
            bufstr += _inp
            ouf.write(bufstr+'\n')
    print('Program working: '+str(time.time()-tm)+' sec'+'\n')


#makefile(1000)
