
# from src.source_file import source_file

class line(object):
    def __init__(self, text: str, sfile, index: int):
        self.text = text
        self.sfile = sfile
        self.index = index
    def copy(me):
        return line(me.text, me.sfile, me.index)
  
    def is_whitespace_or_empty(self): return len(self.text) < 1 or self.text.isspace()
    def get_indent(self) -> str:
        re = ""
        for c in self.text:
            if c.isspace(): re += c
            else: break
        return re

