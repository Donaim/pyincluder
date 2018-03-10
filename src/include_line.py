
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
    def __init__(self, l: line, path: str, target_label_name: str, in_args: str):
        self.line = l
        self.line.sfile.sc.include_list.append(self)

        self.path = path
        self.realpath = path

        self.target_file = None # gonna get it later

        in_args, self.condition_str     = get_next_token_arg(in_args, if_key, if_key_len, None, None, '() ')

        self.target_label_name = target_label_name        
        self.target_label_unique = self.target_label_name is None
        if self.target_label_unique: self.target_label_name = create_random_name()
        
        if self.condition_str is None or self.condition_str.isspace() or len(self.condition_str) == 0:
            self.condition_str = None

    @staticmethod
    def try_create(l: line):
        in_args, path = get_next_token_arg(l.text, include_key, include_key_len, '<', '>', None)
        if path is None: return None
        else:
            realpath = format_path(path)
            if not os.path.isabs(realpath): 
                realpath = find_read_include_path(realpath, l.sfile.dirname, l.sfile.sc.extern_dirs)

            in_args, target_label_name = get_next_token_arg(in_args, at_key, at_key_len, None, None, '() ')
            
            if any(map(lambda inc: inc.target_label_name == target_label_name and inc.realpath == realpath, l.sfile.sc.include_list)):
                print("skipped repeated \"{}\" file".format(realpath))
                return None # dont read repeated files
            
            return in_line(l, realpath, target_label_name, in_args)
    
    def isok(self):
        if self.condition_str is None: return True

        istrue = not self.condition_str.startswith('!')
        lstrip = self.condition_str if istrue else self.condition_str[1:]

        re = lstrip in self.line.sfile.sc.variables

        if istrue: return re
        else: return not re
    
    def read_target(self):
        if self.isok(): # condition is satisfied
            self.target_file.read()
        
