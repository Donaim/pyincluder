
class line(object):
    def __init__(self, text: str, source_file: str):
        self.text = text
        self.source_file = source_file
    def is_whitespace_or_empty(self): return len(self.text) < 1 or self.text.isspace()
    def get_indent(self) -> str:
        re = ""
        for c in self.text:
            if c.isspace(): re += c
            else: break
        return re
    def copy(me):
        return line(me.text, me.source_file)

