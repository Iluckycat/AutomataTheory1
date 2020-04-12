import sys
sys.path.insert(0, '../Generator')
import codeGenerator
import SMCCheck
sys.path.insert(0, '../RegEx')
import regex
import time
import os.path

while True:
    print('1. Generate new file')
    print('2. Check file with RegEx')
    print('3. Check file with SMC')
    print('4. Show time of analyzing')
    print('5. Clear time statistics')
    print('0. Quit')
    print('Make your choice: ')
    c = input()
    if c.isdigit():
        choice = int(c)
        if choice == 1:
            print('How many strings do you want to have in a new file?: ')
            while True:
                numstr = input()
                if numstr.isdigit():
                    _num = int(numstr)
                    break
                else:
                    print('Wrong choice, try again!')
            codeGenerator.makefile(_num)
        elif choice == 2:
            regex.regexchkfile()
        elif choice == 3:
            SMCCheck.SMCCheck()
        elif choice == 4:
            if os.path.isfile('Files/time.txt'):
                times = open('Files/time.txt', 'r')
                for line in times.readlines():
                    print(line.rstrip('\n'))
                print('\n')
                times.close()
            else:
                print('Sorry, but you haven\'t analyzed file yet')
        elif choice == 5:
            times = open('Files/time.txt', 'w')
            times.close()
        elif choice == 0:
            break
        else:
            print('Wrong choice, try again!')
    else:
        print('Wrong choice, try again!')
print('The end! Goodbye')