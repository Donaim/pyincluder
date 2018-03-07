INCLUDE_KEYWORD = "#include"
INCLUDE_LEN = len(INCLUDE_KEYWORD)

MOVE_IMPORTS = True
LEAVE_HEADERS = False

import sys, os

if len(sys.argv) <= 2: raise Exception("arguments missing! usage: \"pyincluder source.file.py output.file.py\"")
source = sys.argv[1]
output   = sys.argv[2]

include_list = []
imports_list = []

class output_scope(object):
    outtext = ""

def collect_whitespace(line: str):
    re = ""
    for c in line:
        if c.isspace(): re += c
        else: break
    return re
    
def format_path(path):
    path = path.replace('/', os.path.sep).replace('\\', os.path.sep)
    if (path[0] == '~' and path[1] == os.path.sep): path = os.path.expanduser('~') + path[1:]
    return path
def get_include_file(line, base_dir):
    filepath = line.lstrip()[INCLUDE_LEN:]
    filepath = filepath.strip()
    if filepath[0] == '<' and filepath[-1] == '>':
        filepath = filepath[1:-1]
        filepath = format_path(filepath)
        if not os.path.isabs(filepath): filepath = os.path.join(base_dir, filepath)
        return filepath
    else:
        return None

def include(line, base_dir):
    indent = collect_whitespace(line)
    filepath = get_include_file(line, base_dir)
    if not filepath: # not a valid include
        simple_write(line)
    else:
        include_file(indent, filepath)

def include_file(indent, filepath):
    if filepath in include_list:
        print("repeated include of \"{}\"".format(filepath))
    if not os.path.exists(filepath):
        print("attempt to include non existing file \"{}\"".format(filepath), file=sys.stderr)
    elif filepath[-1] == os.path.sep: # include dir
        include_list.append(filepath)
        for f in os.listdir(filepath):
            include_file(line, f)
    else: true_include(indent, filepath)

def true_include(indent, filepath):
    include_list.append(filepath)
    print("including \"{}\"".format(filepath))
    if LEAVE_HEADERS: simple_write(indent + '#py-included' + '<' + filepath + '>' + '\n')
    with open(filepath, 'r') as ireader:
        curr_dir = os.path.dirname(filepath)
        for iline in ireader:
            parse_line(indent + iline, curr_dir)

def simple_write(line):
    output_scope.outtext += line
    # writer.write(line)
def is_import_line(strip):
    return strip.startswith("import") or ( strip.startswith("from") and "import" in strip )
def parse_line(line, base_dir):
    strip = line.lstrip(' \t')
    if strip.startswith(INCLUDE_KEYWORD): 
        include(line, base_dir)
        simple_write('\n')
    elif MOVE_IMPORTS and is_import_line(strip):
        if not strip in imports_list: imports_list.append(strip)
    else: simple_write(line)

with open(source, 'r', encoding='utf-8') as reader:
    source_dir = os.path.dirname(source)
    for line in reader:
        parse_line(line, source_dir)

if MOVE_IMPORTS:
    output_scope.outtext = ("".join(imports_list) + '\n') + output_scope.outtext

with open(output, 'w+', encoding="utf-8") as writer:
    writer.write(output_scope.outtext)
