import unittest
from pymakec import *
from test.testbase import TestHarness

class TestCIf(unittest.TestCase, TestHarness):

    def testDefault(self):
        cf = self.createCFile()
        cf.add(cfunction("int", "main", ["int argc", "const char** argv"],[
            cif("argc > 4", [
              cprintf("%s", cstring("Too Many Arguments"))
            ]),
            celseif("argc > 1", [
                cif("argc > 3", [
                    cprintf("%s", "argv[3]")
                ]),
                celseif("argc > 2",[
                    cprintf("%s", "argv[2]")
                ]),
                celse([
                    cprintf("%s", "argv[1]")
                ]),
            ]),
            celse([
                cprintf("%s", cstring("No Arguments"))
            ])
        ]))
        self.compileCFile(cf)

        self.assertEqual(self.runCFile(cf), "No Arguments")
        self.assertEqual(self.runCFile(cf,["A"]), "A")
        self.assertEqual(self.runCFile(cf,["A","B"]), "B")
        self.assertEqual(self.runCFile(cf,["A","B","C"]), "C")
        self.assertEqual(self.runCFile(cf,["A","B","C","D"]), "Too Many Arguments")

if __name__ == '__main__':
    unittest.main()