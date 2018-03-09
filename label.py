
from line import line

class label(line): # label_line
    coll = []
    def __init__(self, l: line):
        label.coll.append(self)
        self.line = line.copy(l)
        self.label = label.get_label_name(l.text)
        self.includes = [] # fill it later
    def get_label_name(text: str) -> str:
        re = ""
        for c in reversed(text):
            if not c.isspace(): re = c + re
            else: break
        return re
    def try_create(l: line):
        if not l.is_whitespace_or_empty() and l.text[-1] == ':': return label(l)
        else: return None