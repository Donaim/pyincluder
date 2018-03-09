
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
    
    @staticmethod
    def try_create(l: line):
        args, name = get_next_token_arg(l.text, label_key, label_key_len, None, None, '()<> ')
        if name is None or name.isspace(): return None
        else: return label(l, name, args)
    @staticmethod
    def create_random(l: line):
        randstr = ''.join(random.choice('ZBOEXTW') for _ in range(16))
        return label(l, randstr, "")