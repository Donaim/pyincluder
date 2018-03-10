
from src.line import line
from src.label import label
from src.include_line import in_line
import os

class scope(object):
    def __init__(self, root_filepath):
        self.root_filepath = root_filepath
        self.root_dirpath = os.path.dirname(self.root_filepath)
        
        self.label_list = []
        self.include_list = []
        self.move_list = []
        self.file_list = []

        self.variables = []
        self.extern_dirs = []
        
    def connect_labels(self):
        def get_labels(name): return filter(lambda lbl: lbl.name == name, self.label_list)
        
        for inc in self.include_list:
            lbl_list = get_labels(inc.target_label_name)
            connected_count = 0
            for lbl in lbl_list:
                lbl.includes.append(inc)
                connected_count += 1
            if connected_count <= 0: raise Exception("label '{}' for included file \"{}\" does not exist!".format(inc.target_label_name, inc.path))
        
        self.move_no_duplicates = []
        for mv in self.move_list:
            lbl_list = get_labels(mv.target_label_name)
            connected_count = 0
            for lbl in lbl_list:
                connected_count += 1
                if any(map(lambda x: line.sameo(x, mv), self.move_no_duplicates)):
                    print("skipped repeated move at \"{}\" in \"{}\"".format(mv.target_label_name, mv.sfile.path))
                    continue # dont read repeated files
                lbl.moves.append(mv)
            if connected_count <= 0: raise Exception("label '{}' for move instruction at {} does not exist!".format(mv.target_label_name, mv.get_pos_string()))
            else: self.move_no_duplicates.append(mv)


        