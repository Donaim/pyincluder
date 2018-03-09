import os

def format_path(path):
    path = path.replace('/', os.path.sep).replace('\\', os.path.sep)
    if (path[0] == '~' and path[1] == os.path.sep): path = os.path.expanduser('~') + path[1:]
    return path