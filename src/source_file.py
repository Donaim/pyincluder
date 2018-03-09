
from src.line import line
from src.label import label
from src.include_line import in_line
from src.scope import scope
from src.outer import outer

import os

class source_file(object):
    def __init__(self, path, sc: scope, indent):
        sc.file_list.append(self)
        self.path = path
        self.dirname = os.path.dirname(self.path)
        self.sc = sc

        self.indent = indent
        self.lines = []
        self.my_includes = []
        # self.my_labels = []
        # self.included_files = []
    @staticmethod
    def create_root(path):
        return source_file(path, scope(), '')
    
    def read(self):
        self.__read_myself()
        
        for x in self.my_includes:
            x.target_file = source_file(x.realpath, self.sc, self.indent + x.indent)
            x.read_target()
    def __read_myself(self):
        with open(self.path, 'r') as reader:
            line_index = 0
            for text_line in reader:
                line_index += 1
                l = line(self.indent + text_line, self, line_index)
 
                x = in_line.try_create(l)
                if not x is None: 
                    self.my_includes.append(x)
                    if x.target_label is None:
                        x.target_label = label(l, x.realpath)
                    self.lines.append(x.target_label)
                    continue
                x = label.try_create(l)
                if not x is None: 
                    self.my_labels.append(x)
                    self.lines.append(x)
                    continue
 
                self.lines.append(l)
    def write_me(self, wr: outer):
        for l in self.lines:
            if type(l) is label:
                for i in l.includes:
                    i.target_file.write_me(wr)
            else:
                wr.write(l.text)