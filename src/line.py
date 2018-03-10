
# from src.source_file import source_file

class line(object):
    def __init__(self, text: str, sfile, index: int):
        self.text = text
        self.sfile = sfile
        self.index = index
    
    @staticmethod
    def init_with(inherited_obj, line_to_copy):
        line.__init__(inherited_obj, line_to_copy.text, line_to_copy.sfile, line_to_copy.index)
        
    def is_whitespace_or_empty(self): return len(self.text) < 1 or self.text.isspace()
    def get_indent(self) -> str:
        re = ""
        for c in self.text:
            if c.isspace(): re += c
            else: break
        return re

