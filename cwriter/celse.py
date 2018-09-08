from .cblock import CBlockGenerator

class CElseGenerator(CBlockGenerator):

    def __init__(self):
        super().__init__()

    def generate(self) :
        return "{}else\n{}".format(
            self.getIndentStr(-1),
            super(CElseGenerator, self).generate()
        )
