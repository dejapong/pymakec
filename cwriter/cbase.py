class CGeneratorBase():

    def __init__(self) :
        self.items = []
        self.indentLvl = 0
        self.indentAmt = 4

    def _generateOrUse(self, item):
        if hasattr(item, "generate"):
            return item.generate()
        else:
            return item

    def getIndentStr(self, offset = 0) :
        return " " * self.indentAmt * (self.indentLvl + offset)

    def add(self, item, before=None, after=None):
        if hasattr(item, "generate"):
            item.indentLvl = self.indentLvl + 1
        else:
            item = self.getIndentStr() + item

        if after is not None and before is not None:
            raise Exception("Cannot set both before and after")

        if before is not None:
            index = self.items.index(before)
            self.items.insert(index, item)
        elif after is not None:
            index = self.items.index(after) + 1
            self.items.insert(index, item)
        else:
            self.items.append(item)

    def addComment(self, comment):
        self.add("/* {} */\n".format(comment))

    def generateDeclaration(self):
        pass

    def generate(self):
        indentedLines = [ self._generateOrUse(item) for item in self.items ]
        return "".join(indentedLines)