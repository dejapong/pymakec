#!/usr/local/bin/python3
from cwriter import *

cf = cfile()

cf.add([
  cinclude("stdio.h", True),
  cinclude("string.h", True),
])

items = cf.add([

  cfunction("int", "main", ["int argc", "const char** argv"], [
    "/* You can always just add strings like this */\n",
    ccomment("Better to add comments this way though"),
    ccall("sayHello", [ cstring(" Hello \"World\" ") ]),
    creturn(0)
  ]),

  cfunction("void", "sayHello", ["const char* helloStr"],[
    cif("helloStr != NULL", [
      cif("strlen(helloStr) > 80", [
        echo("Text is too long to print")
      ]),
      celseif("strlen(helloStr)", [
        cprintf("%s:%d\n", "helloStr", "0")
      ]),
      celse([
        echo("Will not print empty string")
      ])
    ])
  ]),

])

cf.add(items[1].declaration(), before=items[0])
cheader = cheader()
cheader.add(items)

print("\n--- Header File ---\n")
print(cheader.generate())

print("\n--- C File ---\n")
print(cfile.generate())

print("\n--- C File Again! ---\n")
print(cfile.generate())
