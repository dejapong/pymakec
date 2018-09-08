from .cblock import CBlockGenerator

class CElseIfGenerator(CBlockGenerator):

    def __init__(self, condition):
        super().__init__()
        self.condition = condition;

    def generate(self) :
        return "{}else if( {} )\n{}".format(
            self.getIndentStr(-1),
            self.condition,
            super(CElseIfGenerator, self).generate()
        )
