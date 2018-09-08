import unittest
from cwriter import CForGenerator
from test.testbase import TestHarness

class TestCForGenerator(unittest.TestCase, TestHarness):

    def testDefault(self):
        cfile = self.createCFile()
        func_ = cfile.addFunction("int", "main", ["int argc", "const char** argv"])
        for_ = func_.addFor(iLimit = 4)
        for_.addPrintf("%d, ", "i")
        self.assertEqual(self.runCFile(cfile), "0, 1, 2, 3,")

if __name__ == '__main__':
    unittest.main()