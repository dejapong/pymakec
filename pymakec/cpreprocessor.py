
def cinclude(path, system = False):
  fmtString = "#include <{}>\n" if system else "#include \"{}\"\n"
  return fmtString.format(path)