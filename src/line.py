
# from src.source_file import source_file
import os

class line(object):
    def __init__(self, text: str, sfile, index: int):
        self.text = text
        self.sfile = sfile
        self.index = index

    @staticmethod
    def init_with(inherited_obj, line_to_copy):
        line.__init__(inherited_obj, line_to_copy.text, line_to_copy.sfile, line_to_copy.index)
    
    def write_me(self, wr, indent):
        wr.write(indent + self.text)

    def is_whitespace_or_empty(self): return len(self.text) < 1 or self.text.isspace()
    def get_indent(self) -> str:
        re = ""
        for c in self.text:
            if c.isspace(): re += c
            else: break
        return re
    def get_pos(self): return (self.sfile.path, self.index)
    def get_pos_string(self): 
        return 'line:{:>4} in \"{}\"'.format(self.index, os.path.relpath(self.sfile.path, self.sfile.sc.root_dirpath))

    @staticmethod
    def sameo(a, b): # same origin
        return not a.index is None and a.index == b.index and a.sfile.path == b.sfile.path

emptyline = line('', None, -1)
