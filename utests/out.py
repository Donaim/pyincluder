TARGET_INFO='''
hi !
lul lul
'''

DEFAULT_TAG = 'auto'

class tag_funcs(object):
    
    # #include <tags/basic-auto.py>
    ##include <tags/git-auto.py>
    
    ##include <tags/basic.py>
    ##include <tags/git.py>
    
        hi !
        lul lul

    pass

# parsing tag_fucs
tag_funcs_static = filter(lambda name: name[0] != '_', dir(tag_funcs))


# for stderr
import sys

        hi !
        lul lul
class tag(object):
    def __init__(self, name, func):


class arg(object):
    def __init__(self):
        self.command = None
        self.tags = []
    def has_tag(self, tname): return any(map(lambda t: t.name == tname, self.tags))
        self.func = func
    def invoke(self, a):
        try:
            if self.func == None: return False # pure tag, do not invoke
            self.func(a)
            return True
        except ImportError: return False # ignoring those
        except Exception as ex:
            print(ex, file=sys.stderr)
            return False
    def by_name(name):
        if name in tags_dict: return tags_dict[name]
        elif name[0] == '-': return tag(name, None) # pure tag
        else: raise Exception("tag [{}] doesn't have handler!".format(name))
#endmove
def parse_args():
    def is_tag(line: str) -> bool: 
        return line.lstrip()[0] == '$'
    def is_group_tag(aleft: str, aright: str) -> bool: 
        return len(aright) == 0 or aright.isspace()
    def split_tags(line):
        return filter(lambda s: len(s) > 0, (line.replace(' ', ',').replace('\t', ',')).split(','))
    def parse_tags(aleft: str) -> list:
        if len(aleft) == 0: return []
        return list(map(lambda tname: tag.by_name(tname), split_tags(aleft)))
    def find_tag_close(line: str) -> int:
        for (i, c) in enumerate(line):
            if c == ']': return i
        return len(line)
    def split_by_tag(line: str) -> (str, str):
        if is_tag(line):
            line = line.lstrip()[1:] # skip aleft '$' char
            close_index = find_tag_close(line)
            aleft = line[:close_index].strip(' \t,[]')
            aright = line[close_index + 1:].lstrip()
            return (aleft, aright)
        else:
            return ('', line)
    
    #lines
    split = TARGET_INFO.split('\n')
    lines = filter(lambda line: len(line) > 0 and not line.isspace() and line[0] != '#', split)

    #parsing
    group_tags = [tags_dict[DEFAULT_TAG]]
    for line in lines:
        (aleft, aright) = split_by_tag(line)
        if is_group_tag(aleft, aright):
            group_tags = parse_tags(aleft)
        else:
            a = arg()
            a.tags = parse_tags(aleft) + group_tags
            a.command = aright
            args_list.append(a)
    
    #invoking tags
    for a in args_list:
        for t in a.tags:
            if t.invoke(a): return      # if some tag succeded with args, end the program

tags_dict = dict(map(lambda name: (name, tag(name, getattr(tag_funcs, name))), tag_funcs_static))
args_list = []
parse_args()

