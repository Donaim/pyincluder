
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
        line.init_with(self, l)
        self.sfile.sc.move_list.append(self)
        self.target_label_name = at

        self.max_lines = -1
        self.end_index = -1
        max_lines_str = args.strip()
        if max_lines_str.isdigit(): self.max_lines = int(max_lines_str)

    @staticmethod
    def try_create(l: line):
        args, at_arg = get_next_token_arg(l.text, moveat_key, moveat_key_len, None, None, '()<> ')
        if at_arg is None: return None
        else: return moveat(l, at_arg, args)
    
    def read_to(self, output_file):
        def readline_with_check():
            l = original_readline()
            if l is None or l.text.lstrip().startswith(moveat_end_key) or (self.max_lines > 0 and len(self.target_file.lines) >= self.max_lines):
                self.index = l.index
                return None
            else:
                return l
        
        self.target_file = output_file
        original_readline = output_file.read_line_f
        output_file.read_line_f = readline_with_check
        self.target_file.read()

    @staticmethod
    def compare(a, b):
        return a.target_label_name == b.target_label_name and a.line.sfile.path == b.line.sfile.path and a.end_index == b.end_index
    def cmp(self, b): return moveat.compare(self, b)