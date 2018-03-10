
from src.line import line
from src.label import label
from src.include_line import in_line
from src.moveat import moveat
from src.scope import scope
from src.outer import outer
import src.helper

import os

class source_reader(object):
    def __init__(self, path, read_line_f, sc: scope):
        self.read_line_f = read_line_f
        self.path = path
        self.dirname = os.path.dirname(self.path)
        self.sc = sc

        self.lines = []
        self.my_includes = []
        # self.included_files = []
        # self.my_labels = []

        self.after_write = None
    def clear(self):
        self.lines.clear()
        self.my_includes.clear()

    def read(self):
        self.__read_myself()
        
        for x in self.my_includes:
            x.target_file = source_file(x.realpath, self.sc)
            x.read_target()
            
        if not self.after_write is None: self.after_write()
    def __read_myself(self):
        while True:
            l = self.read_line_f()
            if l is None: break

            if not self.__try_create_instructions(l): self.lines.append(l)
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
            x.read_to(source_reader(self.path, self.read_line_f, self.sc)) # write to new virtual file!
            return True
        return False

    def write_me(self, wr: outer, indent: str):
        for l in self.lines:
            if type(l) is label:
                if l.check_condition():
                    for i in l.includes:
                        i.target_file.write_me(wr, indent + l.indent)
                        wr.write('\n')
                    for m in l.moves:
                        m.target_file.write_me(wr, indent + l.indent)
            else:
                wr.write(indent + l.text)


class source_file(source_reader):
    def __init__(self, path, sc: scope):
        sc.file_list.append(self)

        self.reader = open(path, 'r')

        self.line_index = 0
        def std_read_line():
            text = self.reader.readline()
            if not text: return None
            self.line_index += 1
            return line(text, self, self.line_index)
        source_reader.__init__(self, path, std_read_line, sc)

        self.after_write = self.close_file
    def close_file(self):
        if not self.reader.closed:
            self.reader.close()

    @staticmethod
    def create_root(path):
        return source_file(path, scope())