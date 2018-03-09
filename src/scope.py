
from src.label import label
from src.include_line import in_line


class scope(object):
    def __init__(self):
        self.label_list = []
        self.include_list = []
        self.file_list = []
        self.label_dict = {}
    def connect_labels(self):
        label_dict = dict(map(lambda l: (l.label, l.includes), self.label_list))
        
        for inc in self.include_list:
            if inc.target_label.label in label_dict:
                label_dict[inc.target_label.label].append(inc)

        # print("\nLABEL DICT=", label_dict)
        