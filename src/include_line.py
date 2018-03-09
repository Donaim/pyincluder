
import src.config as config
from src.line import line
from src.helper import *

import os

include_key = config.COMMENT_CHARS + 'include'
include_key_len = len(include_key)
at_key = 'at'
at_key_len = len(at_key)
if_key = 'if'
if_key_len = len(if_key)

class in_line(line): # include_line
    def __init__(self, l: line, path: str, in_args: str):
        self.line = l
        self.line.sfile.sc.include_list.append(self)

        self.path = path
        self.realpath = format_path(path)
        if not os.path.isabs(self.realpath): 
            self.realpath = find_read_include_path(self.realpath, self.line.sfile.dirname, self.line.sfile.sc.extern_dirs)

        self.target_file = None # gonna get it later

        in_args, self.target_label_name = get_next_token_arg(in_args, at_key, at_key_len, None, None, '() ')
        in_args, self.condition_str     = get_next_token_arg(in_args, if_key, if_key_len, None, None, '() ')
    
    @staticmethod
    def try_create(l: line):
        in_args, path = get_next_token_arg(l.text, include_key, include_key_len, '<', '>', None)
        if path is None: return None
        else: return in_line(l, path, in_args)
    
    def read_target(self):
        if self.condition_str in self.line.sfile.sc.variables or self.condition_str is None: # condition is satisfied
            self.target_file.read()
        
