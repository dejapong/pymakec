from .cblock import CBlockGenerator

class CFunctionGenerator(CBlockGenerator):

    def __init__(self, returnType, name, argumentList):
        super().__init__()
        self.returnType = returnType
        self.name = name
        self.argumentList = argumentList

    def generatePrototype(self) :
        return "\n{indentStr}{ret} {name} ({argList})".format(
            indentStr = self.getIndentStr(-1),
            ret = self.returnType,
            name = self.name,
            argList = ", ".join(self.argumentList))

    def generateDeclaration(self, indentLvl = 0, indentAmt = 4):
        return "{proto};".format(proto = self.generatePrototype())

    def generate(self) :
        return "{}\n{}".format(self.generatePrototype(), super(CFunctionGenerator, self).generate())