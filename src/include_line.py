
from src.config import config
from src.line import line
from src.helper import *
from src.ifable import ifable
from src.logger import log

import os, sys

include_key = config.COMMENT_CHARS + 'include'
include_key_len = len(include_key)
at_key = 'at'
at_key_len = len(at_key)

class in_line(line, ifable): # include_line
    def __init__(self, l: line, path: str, target_label_name: str, in_args: str):
        line.init_with(self, l)
        ifable.__init__(self)
        self.sfile.sc.include_list.append(self)

        self.path = path
        self.realpath = path

        self.target_file = None # gonna get it later

        in_args = self.parse_condition(in_args)

        self.target_label_name = target_label_name        
        self.target_label_unique = self.target_label_name is None
        if self.target_label_unique: self.target_label_name = create_random_name()

    @staticmethod
    def try_create(l: line):
        # in_args, path = get_next_token_arg(l.text, include_key, include_key_len, '<', '>', None)
        in_args, path = get_next_token_arg(l.text, include_key, include_key_len, None, None, '<>\" ')
        if path is None: return None
        else:
            realpath = format_path(path)
            if not os.path.isabs(realpath): 
                realpath = find_read_include_path(realpath, l.sfile.dirname, l.sfile.sc.extern_dirs)
            if realpath is None or not os.path.exists(realpath):
                if config.ERROR_IF_NO_INCLUDE_EXISTS:
                    raise Exception("path \"{}\" included at {} does not exist!".format(path, l.get_pos_string()))
                else:
                    log.skip_include(l, path, 'LOG$DOES_NOT_EXIST')
                    return None

            in_args, target_label_name = get_next_token_arg(in_args, at_key, at_key_len, None, None, '() ')

            if config.SKIP_REPEATED_FILES and any(map(lambda inc: line.sameo(inc, l), l.sfile.sc.include_list)):
                log.skip_include(l, path, "LOG$REPETITION")
                return None # dont read repeated files
            
            return in_line(l, realpath, target_label_name, in_args)

    def read_target(self):
        if self.check_condition(): # condition is satisfied
            self.target_file.read()
        
