# ex: set ro:
# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : AutomataAnalyzer.sm

import statemap


class AutomataAnalyzerState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def Digit(self, fsm, ch):
        self.Default(fsm)

    def EOS(self, fsm):
        self.Default(fsm)

    def GridSmb(self, fsm):
        self.Default(fsm)

    def LetterL(self, fsm, ch):
        self.Default(fsm)

    def LetterU(self, fsm, ch):
        self.Default(fsm)

    def SpaceSmb(self, fsm):
        self.Default(fsm)

    def SpaseSmb(self, fsm):
        self.Default(fsm)

    def Start(self, fsm):
        self.Default(fsm)

    def TabSmb(self, fsm):
        self.Default(fsm)

    def Unknown(self, fsm):
        self.Default(fsm)

    def Default(self, fsm):
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException(msg)

class MainMap_Default(AutomataAnalyzerState):

    def Start(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.ClearSMC()
        finally:
            fsm.setState(MainMap.Start)
            fsm.getState().Entry(fsm)


    def LetterL(self, fsm, ch):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def LetterU(self, fsm, ch):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def Digit(self, fsm, ch):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def SpaceSmb(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def GridSmb(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def TabSmb(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def Unknown(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


class MainMap_Start(MainMap_Default):

    def GridSmb(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.IncCnt()
        finally:
            fsm.setState(MainMap.Grid)
            fsm.getState().Entry(fsm)


    def SpaseSmb(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(MainMap.Start)
        fsm.getState().Entry(fsm)


class MainMap_Grid(MainMap_Default):

    def LetterL(self, fsm, ch):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.InsToBuf(ch)
            ctxt.IncCnt()
        finally:
            fsm.setState(MainMap.Command)
            fsm.getState().Entry(fsm)


class MainMap_Command(MainMap_Default):

    def LetterL(self, fsm, ch):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.InsToBuf(ch)
            ctxt.IncCnt()
        finally:
            fsm.setState(endState)


    def SpaceSmb(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.CheckCmd() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.InsCmd()
                ctxt.ClearBuf()
                ctxt.IncCnt()
            finally:
                fsm.setState(MainMap.Space1)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.SpaceSmb(self, fsm)
        
class MainMap_Space1(MainMap_Default):

    def LetterU(self, fsm, ch):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.InsToBuf(ch)
            ctxt.IncCnt()
            ctxt.IncLength()
        finally:
            fsm.setState(MainMap.Macros)
            fsm.getState().Entry(fsm)


class MainMap_Macros(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.CheckOP1() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.InsMacros()
                ctxt.ClearBuf()
            finally:
                fsm.setState(MainMap.OK)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.EOS(self, fsm)
        
    def LetterU(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.LessThen10() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.InsToBuf(ch)
                ctxt.IncCnt()
                ctxt.IncLength()
            finally:
                fsm.setState(endState)
        else:
            MainMap_Default.LetterU(self, fsm, ch)
        
    def SpaceSmb(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.InsMacros()
            ctxt.IncCnt()
            ctxt.ClearBuf()
        finally:
            fsm.setState(MainMap.Space2)
            fsm.getState().Entry(fsm)


class MainMap_Space2(MainMap_Default):

    def Digit(self, fsm, ch):
        ctxt = fsm.getOwner()
        if (ctxt.LessThen80()) and (ctxt.CheckOP2()) :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.InsToBuf(ch)
                ctxt.IncCnt()
            finally:
                fsm.setState(MainMap.Operands)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.Digit(self, fsm, ch)
        
    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.CheckOP1() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ClearBuf()
            finally:
                fsm.setState(MainMap.OK)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.EOS(self, fsm)
        
    def LetterL(self, fsm, ch):
        ctxt = fsm.getOwner()
        if (ctxt.LessThen80()) and (ctxt.CheckOP2()) :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.InsToBuf(ch)
                ctxt.IncCnt()
            finally:
                fsm.setState(MainMap.Operands)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.LetterL(self, fsm, ch)
        
    def LetterU(self, fsm, ch):
        ctxt = fsm.getOwner()
        if (ctxt.LessThen80()) and (ctxt.CheckOP2()) :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.InsToBuf(ch)
                ctxt.IncCnt()
            finally:
                fsm.setState(MainMap.Operands)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.LetterU(self, fsm, ch)
        
class MainMap_Operands(MainMap_Default):

    def Digit(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.LessThen80() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.InsToBuf(ch)
                ctxt.IncCnt()
            finally:
                fsm.setState(endState)
        else:
            MainMap_Default.Digit(self, fsm, ch)
        
    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.InsOps()
            ctxt.ClearBuf()
        finally:
            fsm.setState(MainMap.OK)
            fsm.getState().Entry(fsm)


    def LetterL(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.LessThen80() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.InsToBuf(ch)
                ctxt.IncCnt()
            finally:
                fsm.setState(endState)
        else:
            MainMap_Default.LetterL(self, fsm, ch)
        
    def LetterU(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.LessThen80() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.InsToBuf(ch)
                ctxt.IncCnt()
            finally:
                fsm.setState(endState)
        else:
            MainMap_Default.LetterU(self, fsm, ch)
        
    def SpaceSmb(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.LessThen80() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.InsOps()
                ctxt.IncNoe()
                ctxt.IncCnt()
                ctxt.ClearBuf()
            finally:
                fsm.setState(MainMap.Space3)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.SpaceSmb(self, fsm)
        
class MainMap_Space3(MainMap_Default):

    def Digit(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.LessThen80() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.InsToBuf(ch)
                ctxt.IncCnt()
            finally:
                fsm.setState(MainMap.Operands)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.Digit(self, fsm, ch)
        
    def LetterL(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.LessThen80() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.InsToBuf(ch)
                ctxt.IncCnt()
            finally:
                fsm.setState(MainMap.Operands)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.LetterL(self, fsm, ch)
        
    def LetterU(self, fsm, ch):
        ctxt = fsm.getOwner()
        if ctxt.LessThen80() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.InsToBuf(ch)
                ctxt.IncCnt()
            finally:
                fsm.setState(MainMap.Operands)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.LetterU(self, fsm, ch)
        
class MainMap_OK(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.Acceptable()
        finally:
            fsm.setState(endState)


class MainMap_Error(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(endState)


class MainMap(object):

    Start = MainMap_Start('MainMap.Start', 0)
    Grid = MainMap_Grid('MainMap.Grid', 1)
    Command = MainMap_Command('MainMap.Command', 2)
    Space1 = MainMap_Space1('MainMap.Space1', 3)
    Macros = MainMap_Macros('MainMap.Macros', 4)
    Space2 = MainMap_Space2('MainMap.Space2', 5)
    Operands = MainMap_Operands('MainMap.Operands', 6)
    Space3 = MainMap_Space3('MainMap.Space3', 7)
    OK = MainMap_OK('MainMap.OK', 8)
    Error = MainMap_Error('MainMap.Error', 9)
    Default = MainMap_Default('MainMap.Default', -1)

class AutomataAnalyzer_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self, MainMap.Start)
        self._owner = owner

    def __getattr__(self, attrib):
        def trans_sm(*arglist):
            self._transition = attrib
            getattr(self.getState(), attrib)(self, *arglist)
            self._transition = None
        return trans_sm

    def enterStartState(self):
        self._state.Entry(self)

    def getOwner(self):
        return self._owner

# Local variables:
#  buffer-read-only: t
# End:
