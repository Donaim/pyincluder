
from src.line import *
from src.helper import *
from src.config import *
from src.ifable import ifable
from src.config import config
import random

moveat_key = config.COMMENT_CHARS + 'moveat'
moveat_key_len = len(moveat_key)
moveat_end_key = config.COMMENT_CHARS + 'endmove'
moveat_end_key_len = len(moveat_end_key)
at_key = 'at'
at_key_len = len(at_key)

class moveat(line, ifable): # label_line
    def __init__(self, l: line, at: str, args: str):
        line.init_with(self, l)
        ifable.__init__(self)
        self.sfile.sc.move_list.append(self)
        self.target_label_name = at

        self.end_index = -1

        args, self.max_lines = moveat.get_num(args)
        args = self.parse_condition(args)

    @staticmethod
    def get_num(args: str):
        copy = args.lstrip()
        s = ''
        for c in copy:
            if c.isdigit(): s += c

        if len(s) > 0:
            return (copy, int(s))
        else:
            return (args, -1)

    @staticmethod
    def try_create(l: line):
        args, at_arg = get_next_token_arg(l.text, moveat_key, moveat_key_len, None, None, '()<> ')
        if at_arg is None: return None
        else: return moveat(l, at_arg, args)
    
    def read_to(self, output_file):
        def readline_with_check():
            l = original_readline()

            if l is None or l.text.lstrip().startswith(moveat_end_key) or (self.max_lines > 0 and len(self.target_file.lines) >= self.max_lines):
                self.end_index = l.index
                return None
            else:
                if ok: return l
                else: return emptyline
        
        ok = self.check_condition()

        self.target_file = output_file
        original_readline = output_file.read_line_f
        output_file.read_line_f = readline_with_check
        
        self.target_file.read()
        if not ok: self.target_file.clear()