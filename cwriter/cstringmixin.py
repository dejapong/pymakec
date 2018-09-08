from .util import wrapString

class CStringMixin:

  def addEcho(self, text):
    self.addPrintf("%s\n", wrapString(text))

  def addPrintf(self, fmt, *args):
    self.addCall("printf", [ wrapString(fmt) ] + list(args))
