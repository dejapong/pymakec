import subprocess
from cwriter import CFileGenerator, CForGenerator, wrapString

class TestHarness:

  def createCFile(self):
    cfile = CFileGenerator()
    cfile.addInclude("stdio.h", True)
    cfile.addInclude("string.h", True)
    return cfile

  def runCFile(self, cfile):
    basename = type(self).__name__ + ".test";
    execname = basename;
    srcname = basename + ".c";

    # Convert codelist to string.
    codeString = cfile.generate();

    # Print code to output source file
    outfile = open(srcname,'w');
    outfile.write(codeString);
    outfile.close();

    cmd = ["gcc", srcname, "-o", execname];

    p = subprocess.call(cmd);
    self.assertEqual(p, 0);

    output = subprocess.check_output(["./"+execname])
    return output.decode('UTF-8').strip()
