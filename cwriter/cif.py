from .cblock import CBlockGenerator

class CIfGenerator(CBlockGenerator):

    def __init__(self, condition):
        super().__init__()
        self.condition = condition;

    def generate(self) :
        return "{}if( {} )\n{}".format(
            self.getIndentStr(-1),
            self.condition,
            super(CIfGenerator, self).generate()
        )
