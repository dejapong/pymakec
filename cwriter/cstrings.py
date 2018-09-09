from .cbase import cbase
from .cstatements import ccall

def cstring(toWrap):
    fmttd = toWrap
    fmttd = fmttd.replace("\n","\\n")
    fmttd = fmttd.replace("\"","\\\"")
    return str.format("\"{}\"", fmttd)

def cprintf(fmt, *args):
    return ccall("printf", [ cstring(fmt) ] + list(args))

def echo(text):
    return cprintf("%s\n", cstring(text))
