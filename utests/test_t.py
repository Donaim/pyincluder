
import unittest
import pprint
pp = pprint.PrettyPrinter(indent=4)

from src.line import line
from src.label import label
from src.include_line import in_line
from src.source_file import source_file
from src.scope import scope
from src.outer import outer
from src.helper import *
from src.config import config

def format_obj(obj):
    v = vars(obj)
    # if 'line' in v: v['line'] = vars(v['line'])
    return v

class ParsersTest(unittest.TestCase):
    def test_in_line(self):
        l = line("    #include <test_t.py> at kek if(move_imports)", source_file.create_root("utests\\target_info.txt") , 1)
        inc = in_line.try_create(l)
        if not inc is None:
            pp.pprint(format_obj(inc))

        self.assertIsNotNone(inc)
    def test_label(self):
        l = line("#label test_lalba!\nprint(hi) #", source_file.create_root("utests\\target_info.txt"), 1)
        lab = label.try_create(l)
        if not lab is None: 
            pp.pprint(format_obj(lab))

        self.assertIsNotNone(lab)

    def test_sfile(self):
        sf = source_file.create_root("utests\\sample_test_file.py")
        sf.read()

        print("test_file includes:")
        pp.pprint(list(map(lambda x: format_obj(x), sf.sc.include_list)))

    def test_writer(self):
        sf = source_file.create_root("utests\\sample_test_file.py")
        sf.read()
        sf.sc.connect_labels()
        
        wr = outer('utests\\out.py')
        sf.write_me(wr, '')
        wr.close()

    def test_performance(self):
        includer_path = format_path('pyincluder.py')
        infile = format_path('~/Documents/dev/SetTheoryP/main.cpp')
        outfile = format_path('ignore/setoutput.cpp')
        edirs = [
            "C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\VC\\Tools\\MSVC\\14.12.25827\\include", 
            "C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.16299.0\\ucrt",
            "C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.16299.0\\shared"
        ]

        full = ['py'] + [includer_path] + [infile, outfile] + list(map(lambda x: '-I\"{}\"'.format(x), edirs))
        print(' '.join(full))
        return
        
        import subprocess
        subprocess.check_call(full)

    def test_printconfig(self):
        config.printme()



