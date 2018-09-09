from .cbase import cbase
from .cblocks import cfunction

class cfile(cbase):

    def __init__(self, items=[]):
        super().__init__()
        self.add(items)

    def addFunction(self, returnType, name, argumentList):
        function = cfunction(returnType, name, argumentList)
        self.add(function)
        return function

class cheader(cbase):

    def __init__(self):
        super().__init__()

    def generate(self):
        return "\n".join(map(lambda item: item.declaration(), self.items))