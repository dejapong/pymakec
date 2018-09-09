import subprocess
from cwriter import *

class TestHarness:

  def createCFile(self):
    c = cfile([
      cinclude("stdio.h", True),
      cinclude("string.h", True),
    ])
    return c

  def runCFile(self, c):
    basename = type(self).__name__ + ".test";
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

    output = subprocess.check_output(["./"+execname])
    return output.decode('UTF-8').strip()
