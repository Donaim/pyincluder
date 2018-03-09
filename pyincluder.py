import sys, os

if len(sys.argv) <= 2: raise Exception("arguments missing! usage: \"{} <input.file> <output.file> [-options...] [vars...]\"".format(os.path.basename(sys.argv[0])))
source = sys.argv[1]
output   = sys.argv[2]

#imports
from src.line import line
from src.label import label
from src.include_line import in_line
from src.source_file import source_file
from src.scope import scope
from src.outer import outer

sf = source_file.create_root(source)

#parsing args
for arg in sys.argv[3:]:
    if len(arg) > 0 and arg[0] == '-':
        if len(arg) > 1:
            if arg[1] == 'I': 
                sf.sc.extern_dirs.append(arg[2:])
                continue
        raise Exception("Unknown option: \"{}\"".format(arg))
    else: sf.sc.variables.append(arg)
print("VARS={};".format(sf.sc.variables))
print("EDIRS={};".format(sf.sc.extern_dirs))

# reading
sf.read()
sf.sc.connect_labels()

#writing
wr = outer(output)
sf.write_me(wr, '')
wr.close()