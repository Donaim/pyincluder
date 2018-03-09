import os, random

def format_path(path):
    path = path.replace('/', os.path.sep).replace('\\', os.path.sep)
    if (len(path) > 1 and path[0] == '~' and path[1] == os.path.sep): path = os.path.expanduser('~') + path[1:]
    return path
def find_read_include_path(rawpath, current_dir, scope_dirs):
    for d in [current_dir] + scope_dirs:
        path = os.path.join(d, rawpath)
        if os.path.exists(path): return path
    return None

def file_std_append(me, l): me.lines.append(l)

def create_random_name():
    return ''.join(random.choice('ZBOEXTW') for _ in range(16))

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
        while close_index < len(copy) and (copy[close_index].isalpha() or copy[close_index].isdigit()): close_index += 1
    
    re = copy[:close_index]
    re = re.rstrip(ss)
    copy = copy[close_index + 1:]
    copy = copy.lstrip()
    return (copy, re)