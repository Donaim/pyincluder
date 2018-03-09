
from src.label import label
from src.include_line import in_line


class scope(object):
    def __init__(self):
        self.label_list = []
        self.include_list = []
        self.file_list = []
        # self.label_dict = {}
    def connect_labels(self):
        def get_label(name):
            for lab in self.label_list:
                if name == lab.label: return lab
            return None
            
        for inc in self.include_list:
            lbl = get_label(inc.target_label)
            if lbl is None: raise Exception("label '{}' for included file \"{}\" does not exist!".format(inc.target_label, inc.path))
            lbl.includes.append(inc)
        

        