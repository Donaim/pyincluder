
from src.label import label
from src.include_line import in_line


class scope(object):
    def __init__(self):
        self.label_list = []
        self.include_list = []
        self.file_list = []
        # self.label_dict = {}
    def connect_labels(self):
        for inc in self.include_list:
            for lab in self.label_list:
                if inc.target_label.label == lab.label:
                    lab.includes.append(inc)
        

        