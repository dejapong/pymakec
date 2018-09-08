#!/usr/local/bin/python3

from cwriter import CFileGenerator, CHeaderGenerator, wrapString

cheader = CHeaderGenerator()
cfile = CFileGenerator()

cfile.addInclude("stdio.h", True)
cfile.addInclude("string.h", True)

func1 = cfile.addFunction("int", "main", ["int argc", "const char** argv"])
func1.add("/* You can always just add strings like this */\n")
func1.addComment("Better to add comments this way though")
func1.addCall("sayHello", [ wrapString(" Hello \"World\" ") ])
func1.addReturn(0)

func2 = cfile.addFunction("void", "sayHello", ["const char* helloStr"])

ifa = func2.addIf("helloStr != NULL")
ifb = ifa.addIf("strlen(helloStr) > 80")
ifb.addEcho("Text is too long to print")
elsif = ifa.addElseIf("strlen(helloStr)")
elsif.addPrintf("%s:%d\n", "helloStr", "0")
elsa = ifa.addElse()

elsa.addEcho("Text is too long to print")
cfile.add(func2.generateDeclaration(), before=func1)

cheader.add(func1)
cheader.add(func2)

print("\n--- Header File ---\n")
print(cheader.generate())

print("\n--- C File ---\n")
print(cfile.generate())

print("\n--- C File Again! ---\n")
print(cfile.generate())
