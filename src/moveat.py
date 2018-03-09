
from src.line import line
from src.helper import *
from src.config import *
import random

moveat_key = COMMENT_CHARS + 'moveat'
moveat_key_len = len(moveat_key)
moveat_end_key = COMMENT_CHARS + 'endmove'
moveat_end_key_len = len(moveat_end_key)
at_key = 'at'
at_key_len = len(at_key)

class moveat(line): # label_line
    def __init__(self, l: line, at: str, args: str):
        self.line = l
        self.line.sfile.sc.move_list.append(self)
        self.target_label_name = at
        self.lines = [] # fill it later

        self.max_lines = -1
        self.end_index = -1
        max_lines_str = args.strip()
        if max_lines_str.isdigit(): self.max_lines = int(max_lines_str)

    @staticmethod
    def try_create(l: line):
        args, at_arg = get_next_token_arg(l.text, moveat_key, moveat_key_len, None, None, '()<> ')
        if at_arg is None: return None
        else: return moveat(l, at_arg, args)
    
    def __read_callback(self, file, l: line):
        if l.text.lstrip().startswith(moveat_end_key) or (self.max_lines > 0 and len(self.lines) >= self.max_lines):
            self.line.sfile.appendf = file_std_append # end read
            self.end_index = l.index
        else:
            self.lines.append(l)
    def begin_read(self):
        self.line.sfile.appendf = self.__read_callback