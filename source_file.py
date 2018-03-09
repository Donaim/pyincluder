
class source_file(object):
    coll = []
    def __init__(self, path):
        source_file.coll.append(self)
        self.path = path
        self.lines = []
