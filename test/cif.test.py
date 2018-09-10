import unittest
from pymakec import *
from test.testbase import TestHarness

class TestCIf(unittest.TestCase, TestHarness):

    def testDefault(self):
        cf = self.createCFile()
        cf.add(cfunction("int", "main", ["int argc", "const char** argv"],[
            cif("1", items = [
                cprintf("%s", cstring("Hello World"))
            ])
        ]))
        self.compileCFile(cf)
        self.assertEqual(self.runCFile(cf), "Hello World")

if __name__ == '__main__':
    unittest.main()