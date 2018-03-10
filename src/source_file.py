
from src.line import line
from src.label import label
from src.include_line import in_line
from src.moveat import moveat
from src.scope import scope
from src.outer import outer
import src.helper

import os

class source_file(object):
    def __init__(self, path, sc: scope):
        sc.file_list.append(self)
        self.path = path
        self.dirname = os.path.dirname(self.path)
        self.sc = sc

        self.lines = []
        self.my_includes = []
        self.appendf = src.helper.file_std_append
        # self.included_files = []
        # self.my_labels = []
    @staticmethod
    def create_root(path):
        return source_file(path, scope())
    
    def read(self):
        self.__read_myself()
        
        for x in self.my_includes:
            x.target_file = source_file(x.realpath, self.sc)
            x.read_target()
    def __read_myself(self):
        with open(self.path, 'r') as reader:
            line_index = 0
            while True:
                text_line = reader.readline()
                if not text_line: break

                line_index += 1
                l = line(text_line, self, line_index)

                if not self.__try_create_instructions(l): self.appendf(self, l)
    def __try_create_instructions(self, l: line):
        x = in_line.try_create(l)
        if not x is None: 
            self.my_includes.append(x)
            if x.target_label_unique: self.lines.append(label(l, x.target_label_name, ''))
            return True
        x = label.try_create(l)
        if not x is None: 
            # self.my_labels.append(x)
            self.lines.append(x)
            return True
        x = moveat.try_create(l)
        if not x is None:
            x.begin_read()
            return True
        return False

    def write_me(self, wr: outer, indent: str):
        for l in self.lines:
            if type(l) is label:
                if l.isok():
                    for i in l.includes:
                        i.target_file.write_me(wr, indent + l.indent)
                        wr.write('\n')
                    for m in l.moves:
                        for mline in m.lines:
                            wr.write(mline.text)
            else:
                wr.write(indent + l.text)