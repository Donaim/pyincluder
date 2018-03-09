
from line import line
from label import label
from include_line import in_line

class source_file(object):
    coll = []
    def __init__(self, path):
        source_file.coll.append(self)
        self.path = path
        self.lines = []
    
    def read(self):
        with open(self.path, 'r') as reader:
            for text_line in reader:
                l = line(text_line, self)


                self.lines.append(l)