from .cfunction import CFunctionGenerator

class CHeaderGenerator():

    def __init__(self):
        self._items = []
        self.indentAmt = 4
        self.indentLvl = 0

    def add(self, item):
        # TODO check type
        self._items.append(item)

    def addFunction(self, returnType, name, argumentList):
        function = CFunctionGenerator(returnType, name, argumentList)
        self.add(function)
        return function

    def generate(self):
        return "\n".join(map(lambda item: item.generateDeclaration(), self._items))