TARGET_INFO='''
hi !
lul lul
'''

DEFAULT_TAG = 'auto'

    
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

        self.command = None
        self.tags = []
    def has_tag(self, tname): return any(map(lambda t: t.name == tname, self.tags))
        self.name = name
        self.func = func
            if self.func == None: return False # pure tag, do not invoke
            self.func(a)
            return True
        except ImportError: return False # ignoring those
            print(ex, file=sys.stderr)
            return False
        if name in tags_dict: return tags_dict[name]
        elif name[0] == '-': return tag(name, None) # pure tag
        else: raise Exception("tag [{}] doesn't have handler!".format(name)) 
        return line.lstrip()[0] == '$'
        return len(aright) == 0 or aright.isspace()
        return filter(lambda s: len(s) > 0, (line.replace(' ', ',').replace('\t', ',')).split(','))
        if len(aleft) == 0: return []
        return list(map(lambda tname: tag.by_name(tname), split_tags(aleft)))
            if c == ']': return i
        return len(line)
            line = line.lstrip()[1:] # skip aleft '$' char
            close_index = find_tag_close(line)
            aleft = line[:close_index].strip(' \t,[]')
            aright = line[close_index + 1:].lstrip()
            return (aleft, aright)
            return ('', line)
    
    #lines
    split = TARGET_INFO.split('\n')
    lines = filter(lambda line: len(line) > 0 and not line.isspace() and line[0] != '#', split)

    #parsing
    group_tags = [tags_dict[DEFAULT_TAG]]
        (aleft, aright) = split_by_tag(line)
            group_tags = parse_tags(aleft)
            a = arg()
            a.tags = parse_tags(aleft) + group_tags
            a.command = aright
            args_list.append(a)
    
    #invoking tags
            if t.invoke(a): return      # if some tag succeded with args, end the program

tags_dict = dict(map(lambda name: (name, tag(name, getattr(tag_funcs, name))), tag_funcs_static))
args_list = []
parse_args()


