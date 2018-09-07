from .cfunction import CFunctionGenerator
from .cbase import CGeneratorBase

class CFileGenerator(CGeneratorBase):

    def __init__(self):
        super().__init__()

    def addInclude(self, path, system = False) :
      fmtString = "#include <{}>\n" if system else "#include \"{}\"\n"
      self.add(fmtString.format(path))

    def addFunction(self, returnType, name, argumentList):
        function = CFunctionGenerator(returnType, name, argumentList)
        self.add(function)
        return function
