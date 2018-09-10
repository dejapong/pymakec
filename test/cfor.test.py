import unittest
from pymakec import *
from test.testbase import TestHarness

class TestCFor(unittest.TestCase, TestHarness):

    def testDefault(self):
        cf = self.createCFile()
        cf.add(cfunction("int", "main", ["int argc", "const char** argv"],[
            cfor(iLimit = 4, items = [
                cprintf("%d, ", "i")
            ])
        ]))
        self.compileCFile(cf)
        self.assertEqual(self.runCFile(cf), "0, 1, 2, 3,")

if __name__ == '__main__':
    unittest.main()