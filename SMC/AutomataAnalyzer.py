import AutomataAnalyzer_sm


class AutomataAnalyzer:
    def __init__(self):
        self._fsm = AutomataAnalyzer_sm.AutomataAnalyzer_sm(self)
        self._isAcceptable = False
        self._fsm.enterStartState()
        self._bufstr = ''
        self._command = ''
        self._macros = ''
        self._operands = []
        self._counter = 0
        self._length = 0
        self._noe = 0

    def GetCmd(self):
        return  self._command

    def GetMacros(self):
        return self._macros

    def Acceptable(self):
        self._isAcceptable = True

    def Unacceptable(self):
        self._isAcceptable = False

    def Check(self, string):
        self._fsm.Start()
        for c in string:
            if not self._isAcceptable:
                break
            if c.islower():
                self._fsm.LetterL(c)
            elif c.isupper():
                self._fsm.LetterU(c)
            elif c.isdigit():
                self._fsm.Digit(c)
            elif c == ' ':
                self._fsm.SpaceSmb()
            elif c == '/t':
                self._fsm.TabSmb()
            elif c == '#':
                self._fsm.GridSmb()
            elif c == '\n':
                self._fsm.EOS()
                break
            else:
                self._fsm.Unknown()
        self._fsm.EOS()
        return self._isAcceptable

    def InsToBuf(self, string):
        self._bufstr += string

    def IncLength(self):
        self._length += 1

    def IncCnt(self):
        self._counter += 1

    def IncNoe(self):
        self._noe += 1

    def InsCmd(self):
        self._command += self._bufstr

    def InsMacros(self):
        self._macros += self._bufstr

    def InsOps(self):
        self._operands.append(self._bufstr)

    def LessThen10(self):
        return self._length < 10

    def LessThen80(self):
        return self._counter < 79

    def CheckCmd(self):
        a = False
        if self._bufstr == "add" or self._bufstr == "chk" or self._bufstr == "def" or self._bufstr == "und":
            a = True
        return a

    def CheckOP1(self):
        return self._command == 'und' or self._command == 'chk'

    def CheckOP2(self):
        return self._command == 'chk' or self._command == 'add' or self._command == 'def'

    def ClearBuf(self):
        self._bufstr = ''

    def ClearSMC(self):
        self._isAcceptable = True
        self._bufstr = ''
        self._command = ''
        self._macros = ''
        self._operands = []
        self._counter = 0
        self._length = 0
        self._noe = 0
