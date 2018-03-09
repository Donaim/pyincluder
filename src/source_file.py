
from src.line import line
from src.label import label
from src.include_line import in_line

class source_file(object):
    coll = []
    def __init__(self, path):
        source_file.coll.append(self)
        self.path = path
        self.lines = []
    
    def read(self):
        with open(self.path, 'r') as reader:
            line_index = 1
            for text_line in reader:
                l = line(text_line, self, line_index)


                self.lines.append(l)
                line_index += 1