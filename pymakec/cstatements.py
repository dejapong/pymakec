from .cbase import cbase

class cvar(cbase):
    def __init__(self, type_, name, value = None):
        super().__init__()
        self.type_ = type_
        self.name = name
        if value is not None:
            self.value = value
            self.add(value)

    def generate(self):
        if self.value is None:
            return "{} {};\n".format(self.type_, self.name)
        else:
            return "{}{} {} = {};\n".format(
                self.getIndentStr(-1),
                self.type_,
                self.name,
                super(cvar, self).generate().lstrip())

class cassign(cbase):
    def __init__(self, target, value):
        super().__init__()
        self.target = target
        self.add(value)

    def generate(self):
        return "{}{} = {}".format(
            self.getIndentStr(-1),
            self.target,
            super(cassign, self).generate().lstrip())

def creturn(retVal):
    return "return {};\n".format(retVal)

def ccall(funcName, params):
    return "{}({});\n".format(funcName, ", ".join(params))

