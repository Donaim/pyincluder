
from src.line import line
from src.helper import *
from src.config import *
import random

label_key = COMMENT_CHARS + 'label'
label_key_len = len(label_key)
if_key = 'if'
if_key_len = len(if_key)

class label(line): # label_line
    def __init__(self, l: line, lname: str, args: str):
        self.line = l
        self.line.sfile.sc.label_list.append(self)
        self.name = lname
        self.indent = self.line.get_indent()
        self.includes = [] # fill it later

        args, self.condition_str     = get_next_token_arg(args, if_key, if_key_len, None, None, '() ')
        if self.condition_str is None or self.condition_str.isspace() or len(self.condition_str) == 0:
            self.condition_str = None
    def isok(self):
        if self.condition_str is None: return True
        re = self.condition_str in self.line.sfile.sc.variables

        if self.condition_str.startswith('!'): return not re
        else: return re

    @staticmethod
    def try_create(l: line):
        args, name = get_next_token_arg(l.text, label_key, label_key_len, None, None, '()<> ')
        if name is None or name.isspace(): return None
        else: return label(l, name, args)
    @staticmethod
    def create_random(l: line):
        randstr = ''.join(random.choice('ZBOEXTW') for _ in range(16))
        return label(l, randstr, "")

    