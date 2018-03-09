
import unittest
import pprint
pp = pprint.PrettyPrinter(indent=4)

from src.line import line
from src.label import label
from src.include_line import in_line
from src.source_file import source_file

def format_obj(obj):
    v = vars(obj)
    # if 'line' in v: v['line'] = vars(v['line'])
    return v

class ParsersTest(unittest.TestCase):
    def test_in_line(self):
        l = line("    #include <hello.txt> at kek if(move_imports)", source_file("bebe.py", '') , 1)
        inc = in_line.try_create(l)
        if not inc is None:
            pp.pprint(format_obj(inc))

        self.assertIsNotNone(inc)
    def test_label(self):
        l = line("print(hi) #  some_label:", source_file("bebe.py", ''), 1)
        lab = label.try_create(l)
        if not lab is None: 
            pp.pprint(format_obj(lab))

        self.assertIsNotNone(lab)

    def test_sfile(self):
        in_line.coll = []
     
        f = "utests\\sample_test_file.py"
        sf = source_file(f, '')
        sf.read()

        print("test_file includes:")
        pp.pprint(list(map(lambda x: format_obj(x), in_line.coll)))
