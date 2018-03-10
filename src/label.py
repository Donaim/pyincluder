
from src.line import line
from src.helper import *
from src.config import *
from src.ifable import ifable

label_key = COMMENT_CHARS + 'label'
label_key_len = len(label_key)

class label(line, ifable): # label_line
    def __init__(self, l: line, lname: str, args: str):
        line.init_with(self, l)
        ifable.__init__(self)
        self.sfile.sc.label_list.append(self)
        self.name = lname
        self.indent = self.get_indent()
        self.includes = [] # fill it later
        self.moves = [] # fill later

        args = self.parse_condition(args)
    @staticmethod
    def try_create(l: line):
        args, name = get_next_token_arg(l.text, label_key, label_key_len, None, None, '()<> ')
        if name is None or name.isspace(): return None
        else: return label(l, name, args)

    def write_me(self, wr, indent):
        if self.check_condition():
            for i in self.includes:
                i.target_file.write_me(wr, indent + self.indent)
                wr.write('\n')
            for m in self.moves:
                m.target_file.write_me(wr, indent + self.indent)
        

    