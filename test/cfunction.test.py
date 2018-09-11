import unittest
from pymakec import *
from test.testbase import TestHarness

class TestCFunction(TestHarness, unittest.TestCase):

    def testCFunction(self):
        cf = self.createCFile()

        main = cf.add(cfunction("int", "main", ["int argc", "const char** argv"],[
            cvar("int", "retVal", "-1"),
            cassign("retVal", ccall("sayHello", [cstring("Hi There!")])),
            creturn("retVal")
        ]))[0]

        sayHello = cf.add(cfunction("int", "sayHello", ["const char* msg"],[
            cprintf("%s", "msg"),
            creturn(0)
        ]))[0]

        cf.add(sayHello.declaration(), before=main)

        self.compileCFile(cf)
        self.assertEqual(self.runCFile(cf), "Hi There!")

if __name__ == '__main__':
    unittest.main()