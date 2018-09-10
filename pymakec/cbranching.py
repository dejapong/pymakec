from .cblocks import cblock

class cif(cblock):

    def __init__(self, condition, items=[]):
        super().__init__(items)
        self.condition = condition

    def generate(self) :
        return "{}if ( {} )\n{}".format(
            self.getIndentStr(-1),
            self.condition,
            super(cif, self).generate()
        )

class celse(cblock):

    def __init__(self, items=[]):
        super().__init__(items)

    def generate(self) :
        return "{}else\n{}".format(
            self.getIndentStr(-1),
            super(celse, self).generate()
        )

class celseif(cblock):

    def __init__(self, condition, items=[]):
        super().__init__(items)
        self.condition = condition;

    def generate(self) :
        return "{}else if( {} )\n{}".format(
            self.getIndentStr(-1),
            self.condition,
            super(celseif, self).generate()
        )
