from .cblocks import cblock

def ccomment(text):
  return ("/* {} */\n".format(text.replace("*/","* /")))
