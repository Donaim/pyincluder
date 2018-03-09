
import unittest
import pprint
pp = pprint.PrettyPrinter(indent=4)

from src.line import line
from src.label import label
from src.include_line import in_line
from src.source_file import source_file

class ParsersTest(unittest.TestCase):
    def test_in_line(self):
        l = line("    #include <hello.txt> at kek if(move_imports)", "bebe.py")
        inc = in_line.try_create(l)
        if not inc is None:
            v = vars(inc)
            v['line'] = vars(v['line'])
            pp.pprint(v)

        self.assertIsNotNone(inc)
    def test_label(self):
        l = line("print(hi) #  some_label:", "bebe.py")
        lab = label.try_create(l)
        if not lab is None: 
            v = vars(lab)
            v['line'] = vars(v['line'])
            pp.pprint(v)

        self.assertIsNotNone(lab)

    def test_sfile(self):
        f = "utests\\sample_test_file.py"
        sf = source_file(f)
        sf.read()