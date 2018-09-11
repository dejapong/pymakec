import unittest
from pymakec import *
from test.testbase import TestHarness

class TestCFor(TestHarness, unittest.TestCase):

    def testCFor(self):
        cf = self.createCFile()
        cf.add(cfunction("int", "main", ["int argc", "const char** argv"],[
            cfor(iLimit = 4, items = [
                cprintf("%d, ", "i")
            ]),
            creturn(0)
        ]))
        self.compileCFile(cf)
        self.assertEqual(self.runCFile(cf), "0, 1, 2, 3,")

if __name__ == '__main__':
    unittest.main()