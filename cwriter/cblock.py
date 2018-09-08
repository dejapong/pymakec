from .cbase import CGeneratorBase

class CBlockGenerator(CGeneratorBase):

    def __init__(self):
        super().__init__()

    def addIf(self, condition):
        item = CIfGenerator(condition)
        self.add(item)
        return item

    def addElseIf(self, condition):
        item = CElseIfGenerator(condition)
        self.add(item)
        return item

    def addElse(self):
        item = CElseGenerator()
        self.add(item)
        return item

    def addFor(self, iType="int", iName="i", iValue=0, iLimit=1, iStride=1, expr=None):
        item = CForGenerator(iType,iName,iValue,iLimit,iStride,expr)
        self.add(item)
        return item

    def addCall(self, funcName, params):
        item = "{}({});\n".format(funcName, ", ".join(params))
        self.add(item)
        return item

    def addReturn(self, value):
        item = "return {};\n".format(value)
        self.add(item)
        return item

    def generate(self):
        indentStr = self.getIndentStr(-1)
        return "{}{{\n{}{}}}\n".format(
            indentStr,
            super(CBlockGenerator, self).generate(),
            indentStr)

# Imports of components which extend CBlockGenerator need to appear after the class definition
from .cif import CIfGenerator
from .celseif import CElseIfGenerator
from .celse import CElseGenerator
from .cfor import CForGenerator
