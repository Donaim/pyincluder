
import src.config as config
from src.line import line
import src.helper

import os

include_key = config.COMMENT_CHARS + 'include'
include_key_len = len(include_key)
at_key = 'at'
at_key_len = len(at_key)
if_key = 'if'
if_key_len = len(if_key)
def get_next_token_arg(text, name, name_len, open_char, close_char, ss):
    copy = text.lstrip()
    if not copy.startswith(name): return (text, None)
    
    copy = copy[name_len:]
    copy = copy.lstrip()
    if open_char != None:
        if copy[0] != open_char: raise Exception("bad include syntax: {} token argument has to begin with '{}' !".format(name, open_char))
        copy = copy[1:]
    copy = copy.lstrip(ss)
    if close_char != None:
        close_index = copy.find(close_char)
        if close_index == -1: raise Exception("bad include syntax: {} token argument has to end with '{}' !".format(name, close_char))
    else:
        close_index = 0
        while close_index < len(copy) and not copy[close_index].isspace(): close_index += 1
    
    re = copy[:close_index]
    re = re.rstrip(ss)
    copy = copy[close_index + 1:]
    copy = copy.lstrip()
    return (copy, re)

class in_line(line): # include_line
    def __init__(self, l: line, path: str, in_args: str):
        self.line = l
        self.line.sfile.sc.include_list.append(self)
        self.indent = l.get_indent()

        self.path = path
        self.realpath = src.helper.format_path(path)
        if not os.path.isabs(self.realpath): self.realpath = os.path.join(self.line.sfile.dirname, path)
        self.target_file = None # gonna get it later

        in_args, self.target_label = get_next_token_arg(in_args, at_key, at_key_len, None, None, '() ')
        in_args, self.condition    = get_next_token_arg(in_args, if_key, if_key_len, None, None, '() ')
    
    @staticmethod
    def try_create(l: line):
        in_args, path = get_next_token_arg(l.text, include_key, include_key_len, '<', '>', None)
        if path is None: return None
        else: return in_line(l, path, in_args)
    
    def read_target(self): self.target_file.read()
