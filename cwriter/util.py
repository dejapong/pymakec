def wrapString(toWrap):
  fmttd = toWrap
  fmttd = fmttd.replace("\n","\\n")
  fmttd = fmttd.replace("\"","\\\"")
  return str.format("\"{}\"", fmttd)
