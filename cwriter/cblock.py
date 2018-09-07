from .cbase import CGeneratorBase

class CBlockGenerator(CGeneratorBase):

    def __init__(self):
        super().__init__()

    def addCall(self, funcName, params):
        line = "{}({});\n".format(funcName, ", ".join(params))
        self.add(line)
        return line

    def addReturn(self, value):
        line = "return {};".format(value)
        self.add(line)
        return line

    def generate(self):
        indentStr = self.getIndentStr(-1)
        return "{}{{\n{}\n{}}}\n".format(
            indentStr,
            super(CBlockGenerator, self).generate(),
            indentStr)