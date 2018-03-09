
import unittest
import pprint
pp = pprint.PrettyPrinter(indent=4)

from line import line
from label import label
from include_line import in_line
from source_file import source_file

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
        f = "test_sfile.py"
        sf = source_file(f)
        sf.read()
        # pp.pprint(list(map(lambda x: x.text, sf.lines)))

if __name__ == '__main__':
    unittest.main()