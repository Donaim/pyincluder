INCLUDE_KEYWORD = "#include"

LEAVE_HEADERS = False

import sys, os

# if len(sys.argv) <= 2: raise Exception("arguments missing! usage: \"pyincluder source.file.py output.file.py\"")
# source = sys.argv[1]
# output   = sys.argv[2]

class output_scope(object):
    outtext = ""

class line(object):
    def __init__(self, text):
        self.text = text
class include_label(line):
    coll = []
    def __init__(self, text):
        include_label.coll.append(self)
        self.line = line(text)
        self.label = NotImplemented
        self.includes = []
class include_line(line):
    coll = []
    def __init__(self, text):
        include_line.coll.append(self)
        self.line = line(text)
        self.indent = collect_whitespace(text)

        wtext = text.lstrip()[1:] # skip indent and '#' symbol
        (wtext, self.include_file) = include_line.get_next_token_arg(wtext, include_line.include_key, include_line.include_key_len, '<', '>', None)
        (wtext, self.target_label) = include_line.get_next_token_arg(wtext, include_line.at_key, include_line.at_key_len, None, None, '() ')
        (wtext, self.condition)    = include_line.get_next_token_arg(wtext, include_line.if_key, include_line.if_key_len, None, None, '() ')
    
    include_key = "include"
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

def collect_whitespace(line: str):
    re = ""
    for c in line:
        if c.isspace(): re += c
        else: break
    return re

iline = include_line("    #include <hello.txt> if (move_imports)")
print(vars(iline))
    
# def format_path(path):
#     path = path.replace('/', os.path.sep).replace('\\', os.path.sep)
#     if (path[0] == '~' and path[1] == os.path.sep): path = os.path.expanduser('~') + path[1:]
#     return path
# def get_include_file(line, base_dir):
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
#     filepath = get_include_file(line, base_dir)
#     if not filepath: # not a valid include
#         simple_write(line)
#     else:
#         include_file(indent, filepath)

# def include_file(indent, filepath):
#     if filepath in include_list:
#         print("repeated include of \"{}\"".format(filepath))
#     if not os.path.exists(filepath):
#         print("attempt to include non existing file \"{}\"".format(filepath), file=sys.stderr)
#     elif filepath[-1] == os.path.sep: # include dir
#         include_list.append(filepath)
#         for f in os.listdir(filepath):
#             include_file(line, f)
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
