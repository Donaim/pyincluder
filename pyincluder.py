import sys, os

# if len(sys.argv) <= 2: raise Exception("arguments missing! usage: \"pyincluder source.file.py output.file.py\"")
source = sys.argv[1]
# output   = sys.argv[2]

from src.line import line
from src.label import label
from src.include_line import in_line
from src.source_file import source_file

