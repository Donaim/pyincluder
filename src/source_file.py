
from src.line import line
from src.label import label
from src.include_line import in_line
import src.helper

import os

class source_file(object):
    coll = []
    def __init__(self, path, indent):
        source_file.coll.append(self)
        self.path = path
        self.dirname = os.path.dirname(self.path)

        self.indent = indent
        self.lines = []
        self.my_includes = []
        self.my_labels = []
        self.included_files = []
    
    def read(self):
        self.__read_myself()
        
        for x in self.my_includes:
            target_file = source_file(x.realpath, self.indent + x.indent)
            target_file.read()
            self.included_files.append(target_file)
    def __read_myself(self):
        with open(self.path, 'r') as reader:
            line_index = 0
            for text_line in reader:
                line_index += 1
                l = line(text_line, self, line_index)
 
                x = in_line.try_create(l)
                if not x is None: 
                    self.my_includes.append(x)
                    if x.target_label is None:
                        x.target_label = label(l, x.realpath)
                    continue
                x = label.try_create(l)
                if not x is None: 
                    self.my_labels.append(x)
                    self.lines.append(x)
                    continue
 
                self.lines.append(l)