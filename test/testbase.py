import subprocess
from pymakec import *

class TestHarness:

    def setUp(self):
        print (self._testMethodName)

    def _getBaseName(self):
        return type(self).__name__ + ".test"

    def createCFile(self):
        c = cfile([
          cinclude("stdio.h", True),
          cinclude("string.h", True),
        ])
        return c

    def compileCFile(self, c):
        basename = self._getBaseName()
        execname = basename;
        srcname = basename + ".c";

        # Convert codelist to string.
        codeString = c.generate();

        # Print code to output source file
        outfile = open(srcname,'w');
        outfile.write(codeString);
        outfile.close();

        cmd = ["gcc", srcname, "-o", execname];

        p = subprocess.call(cmd);
        self.assertEqual(p, 0);

    def runCFile(self, c, args = []):
        output = subprocess.check_output(["./"+self._getBaseName()] + args)
        return output.decode('UTF-8').strip()
