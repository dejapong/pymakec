def creturn(retVal):
    return "return {};\n".format(retVal)

def ccall(funcName, params):
    return "{}({});\n".format(funcName, ", ".join(params))