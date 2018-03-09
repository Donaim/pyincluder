
from src.line import line
import random



def get_label_name(text: str) -> str:
    re = ""
    for c in reversed(text):
        if not c.isspace(): re = c + re
        else: break
    return re[:-1]

class label(line): # label_line
    def __init__(self, l: line, lname: str):
        self.line = l
        self.line.sfile.sc.label_list.append(self)
        self.label = lname
        self.indent = self.line.get_indent()
        self.includes = [] # fill it later
    
    @staticmethod
    def try_create(l: line):
        if not l.is_whitespace_or_empty():
            rstr =l.text.rstrip()
            if rstr[-1] == ':':
                return label(l, get_label_name(rstr))
        return None
    @staticmethod
    def create_random(l: line):
        randstr = ''.join(random.choice('ZBOEXTW') for _ in range(16))
        return label(l, randstr)