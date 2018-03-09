
from src.line import line
from src.helper import *
from src.config import *
import random

moveat_key = COMMENT_CHARS + 'move'
moveat_key_len = len(moveat_key)
moveat_end_key = COMMENT_CHARS + 'endmove'
moveat_end_key_len = len(moveat_end_key)
at_key = 'at'
at_key_len = len(at_key)

class moveat(line): # label_line
    def __init__(self, l: line, at: str):
        self.line = l
        self.line.sfile.sc.move_list.append(self)
        self.target_label_name = at
        self.lines = [] # fill it later

    @staticmethod
    def try_create(l: line):
        args, at_arg = get_next_token_arg(l.text, moveat_key, moveat_key_len, None, None, '()<> ')
        if at_arg is None or at_arg.isspace(): return None
        else: return moveat(l, at_arg)
    
    def append(self, l: line):
        if l.text.lstrip().startswith(moveat_end_key):
            return None
        self.lines.append(l)
        return self