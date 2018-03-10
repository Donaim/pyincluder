
from src.helper import *

if_key = 'if'
if_key_len = len(if_key)

class ifable(object):
    def __init__(self): 
        pass
    
    def parse_condition(self, args: str):
        args, self.condition_str     = get_next_token_arg(args, if_key, if_key_len, None, None, '() ')
        if self.condition_str is None or self.condition_str.isspace() or len(self.condition_str) == 0:
            self.condition_str = None
        return args
    def isok(self):
        if self.condition_str is None: return True

        negated = self.condition_str.startswith('!')
        lstrip = self.condition_str
        if negated: lstrip = lstrip[1:]

        re = lstrip in self.sfile.sc.variables

        if negated: return not re
        else: return re