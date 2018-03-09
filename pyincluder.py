COMMENT_CHARS = '#'    # can also be '//' or '--'
LEAVE_HEADERS = False

import sys, os

# if len(sys.argv) <= 2: raise Exception("arguments missing! usage: \"pyincluder source.file.py output.file.py\"")
# source = sys.argv[1]
# output   = sys.argv[2]

class output_scope(object):
    outtext = ""

class line(object):
    def __init__(self, text: str, source_file: str):
        self.text = text
        self.source_file = source_file
    def is_whitespace_or_empty(self): return len(self.text) < 1 or self.text.isspace()
    def get_indent(self) -> str:
        re = ""
        for c in self.text:
            if c.isspace(): re += c
            else: break
        return re
    def copy(me):
        return line(me.text, me.source_file)
class label(line): # label_line
    coll = []
    def __init__(self, l: line):
        label.coll.append(self)
        self.line = line.copy(l)
        self.label = label.get_label_name(l.text)
        self.includes = [] # fill it later
    def get_label_name(text: str) -> str:
        re = ""
        for c in reversed(text):
            if not c.isspace(): re = c + re
            else: break
        return re
    def try_create(l: line):
        if not l.is_whitespace_or_empty() and l.text[-1] == ':': return label(l)
        else: return None
class in_line(line): # include_line
    coll = []
    def __init__(self, l: line, path: str, in_args: str):
        in_line.coll.append(self)
        self.line = line.copy(l)
        self.indent = l.get_indent()

        self.path = path
        in_args, self.target_label = in_line.get_next_token_arg(in_args, in_line.at_key, in_line.at_key_len, None, None, '() ')
        in_args, self.condition    = in_line.get_next_token_arg(in_args, in_line.if_key, in_line.if_key_len, None, None, '() ')
    def try_create(l: line):
        in_args, path = in_line.get_next_token_arg(l.text, in_line.include_key, in_line.include_key_len, '<', '>', None)
        if path is None: return None
        else: return in_line(l, path, in_args)

    include_key = COMMENT_CHARS + 'include'
    include_key_len = len(include_key)
    at_key = 'at'
    at_key_len = len(at_key)
    if_key = 'if'
    if_key_len = len(if_key)
    def get_next_token_arg(text, name, name_len, open_char, close_char, ss):
        copy = text.lstrip()
        if not copy.startswith(name): return (text, None)
        
        copy = copy[name_len:]
        copy = copy.lstrip()
        if open_char != None:
            if copy[0] != open_char: raise Exception("bad include syntax: {} token argument has to begin with '{}' !".format(name, open_char))
            copy = copy[1:]
        copy = copy.lstrip(ss)
        if close_char != None:
            close_index = copy.find(close_char)
            if close_index == -1: raise Exception("bad include syntax: {} token argument has to end with '{}' !".format(name, close_char))
        else:
            close_index = 0
            while close_index < len(copy) and not copy[close_index].isspace(): close_index += 1
        
        re = copy[:close_index]
        re = re.rstrip(ss)
        copy = copy[close_index + 1:]
        copy = copy.lstrip()
        return (copy, re)
class source_file(object):
    coll = []
    def __init__(self, path):
        source_file.coll.append(self)
        self.path = path
        self.lines = []

l = line("    #include <hello.txt> at kek if(move_imports)", "bebe.py")
inc = in_line.try_create(l)
if not inc is None:
    print(vars(inc))
else: 
    print('inc is None!')

l = line("print(hi) #  some_label:", "bebe.py")
lab = label.try_create(l)
if not lab is None: 
    print(vars(lab))
else: 
    print("lab is None!")

# def format_path(path):
#     path = path.replace('/', os.path.sep).replace('\\', os.path.sep)
#     if (path[0] == '~' and path[1] == os.path.sep): path = os.path.expanduser('~') + path[1:]
#     return path
# def get_path(line, base_dir):
#     filepath = line.lstrip()[INCLUDE_LEN:]
#     filepath = filepath.strip()
#     if filepath[0] == '<' and filepath[-1] == '>':
#         filepath = filepath[1:-1]
#         filepath = format_path(filepath)
#         if not os.path.isabs(filepath): filepath = os.path.join(base_dir, filepath)
#         return filepath
#     else:
#         return None

# def include(line, base_dir):
#     indent = collect_whitespace(line)
#     filepath = get_path(line, base_dir)
#     if not filepath: # not a valid include
#         simple_write(line)
#     else:
#         path(indent, filepath)

# def path(indent, filepath):
#     if filepath in include_list:
#         print("repeated include of \"{}\"".format(filepath))
#     if not os.path.exists(filepath):
#         print("attempt to include non existing file \"{}\"".format(filepath), file=sys.stderr)
#     elif filepath[-1] == os.path.sep: # include dir
#         include_list.append(filepath)
#         for f in os.listdir(filepath):
#             path(line, f)
#     else: true_include(indent, filepath)

# def true_include(indent, filepath):
#     include_list.append(filepath)
#     print("including \"{}\"".format(filepath))
#     if LEAVE_HEADERS: simple_write(indent + '#py-included' + '<' + filepath + '>' + '\n')
#     with open(filepath, 'r') as ireader:
#         curr_dir = os.path.dirname(filepath)
#         for iline in ireader:
#             parse_line(indent + iline, curr_dir)

# def simple_write(line):
#     output_scope.outtext += line
#     # writer.write(line)
# def is_import_line(strip):
#     return strip.startswith("import") or ( strip.startswith("from") and "import" in strip )
# def parse_line(line, base_dir):
#     strip = line.strip()
#     if strip.endswith("#pyincluder-ignore"):
#         simple_write(line)
#     elif strip.startswith(INCLUDE_KEYWORD):
#         include(line, base_dir)
#         simple_write('\n')
#     else:
#         simple_write(line)

# with open(source, 'r', encoding='utf-8') as reader:
#     source_dir = os.path.dirname(source)
#     for line in reader:
#         parse_line(line, source_dir)

# with open(output, 'w+', encoding="utf-8") as writer:
#     writer.write(output_scope.outtext)
