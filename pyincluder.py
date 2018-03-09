import sys, os

# if len(sys.argv) <= 2: raise Exception("arguments missing! usage: \"pyincluder source.file.py output.file.py\"")
source = sys.argv[1]
# output   = sys.argv[2]

from line import line
from label import label
from include_line import in_line
from source_file import source_file

