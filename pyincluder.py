import sys, os

# if len(sys.argv) <= 2: raise Exception("arguments missing! usage: \"pyincluder source.file.py output.file.py\"")
# source = sys.argv[1]
# output   = sys.argv[2]

from line import line
from label import label
from include_line import in_line
from source_file import source_file

class OUTPUT(object):
    text = ""
    def write(t: str): OUTPUT.text += t

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
#     OUTPUT.text += line
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
#     writer.write(OUTPUT.text)
