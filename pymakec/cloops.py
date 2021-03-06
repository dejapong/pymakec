from .cblocks import cblock

class cfor(cblock):

    def __init__(self, iType="int", iName="i", iValue=0, iLimit=1, iStride=1, expr=None, items=[]):
        super().__init__(items)
        if expr is not None:
          self.expr = expr
        else:
          self.expr = "{} {} = {}; {} < {}; {} += {}".format(iType, iName, iValue, iName, iLimit, iName, iStride)

    def generate(self) :
        return "{}for ( {} )\n{}".format(
            self.getIndentStr(-1),
            self.expr,
            super(cfor, self).generate()
        )
