
from src.label import label
from src.include_line import in_line


class scope(object):
    def __init__(self):
        self.label_list = []
        self.include_list = []
        self.move_list = []
        self.file_list = []

        self.variables = []
        self.extern_dirs = []
    def connect_labels(self):
        def get_label(name):
            for lab in self.label_list:
                if name == lab.name: return lab
            return None
        # print("LABELS:[{}]".format(",".join(map(lambda l: l.name, self.label_list))))

        for inc in self.include_list:
            lbl = get_label(inc.target_label_name)
            if lbl is None: raise Exception("label '{}' for included file \"{}\" does not exist!".format(inc.target_label_name, inc.path))
            lbl.includes.append(inc)
        for mv in self.move_list:
            lbl = get_label(mv.target_label_name)
            if lbl is None: raise Exception("label '{}' for move instruction at line {} in file \"{}\" does not exist!".format(mv.target_label_name, mv.line.index, mv.line.sfile.path))
            lbl.moves.append(mv)
    

        