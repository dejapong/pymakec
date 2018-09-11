from .cbase import cbase

class cblock(cbase):

    def __init__(self, items=[]):
        super().__init__()
        self.add(items)

    def generate(self):
        indentStr = self.getIndentStr(-1)
        return "{}{{\n{}{}}}\n".format(
            indentStr,
            super(cblock, self).generate(),
            indentStr)

class cfunction(cblock):

    def __init__(self, returnType, name, argumentList, items=[]):
        super().__init__(items)
        self.returnType = returnType
        self.name = name
        self.argumentList = argumentList

    def generatePrototype(self) :
        return "\n{ret} {name} ({argList})".format(
            ret = self.returnType,
            name = self.name,
            argList = ", ".join(self.argumentList))

    def declaration(self, indentLvl = 0, indentAmt = 4):
        return "{proto};".format(proto = self.generatePrototype())

    def generate(self) :
        return "{}\n{}".format(self.generatePrototype(), super(cfunction, self).generate())

