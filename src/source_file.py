
from src.line import line
from src.label import label
from src.include_line import in_line
from src.moveat import moveat
from src.scope import scope
from src.outer import outer

import os

class source_file(object):
    def __init__(self, path, sc: scope):
        sc.file_list.append(self)
        self.path = path
        self.dirname = os.path.dirname(self.path)
        self.sc = sc

        self.lines = []
        self.my_includes = []
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
        current_move: moveat = None
        with open(self.path, 'r') as reader:
            line_index = 0
            while True:
                text_line = reader.readline()
                if not text_line: break

                line_index += 1
                l = line(text_line, self, line_index)

                x = in_line.try_create(l)
                if not x is None: 
                    self.my_includes.append(x)
                    rand_lbl = label.create_random(l)
                    if x.target_label_name is None: x.target_label_name = rand_lbl.name
                    self.lines.append(rand_lbl)
                    continue
                x = label.try_create(l)
                if not x is None: 
                    # self.my_labels.append(x)
                    self.lines.append(x)
                    continue
                if current_move is None:
                    current_move = moveat.try_create(l)

                if current_move is None:
                    self.lines.append(l)
                else: 
                    current_move = current_move.append(l)

    def write_me(self, wr: outer, indent: str):
        for l in self.lines:
            if type(l) is label and l.isok():
                for i in l.includes:
                    i.target_file.write_me(wr, indent + l.indent)
                    wr.write('\n')
                for m in l.moves:
                    for mline in m.lines:
                        wr.write(mline.text)
                    wr.write('\n')
            else:
                wr.write(indent + l.text)