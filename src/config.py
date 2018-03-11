
class config:
    COMMENT_CHARS = '#'    # can also be '//' or '--'
    LEAVE_HEADERS = False
    SKIP_REPEATED_FILES = True
    ERROR_IF_NO_INCLUDE_EXISTS = True

    @staticmethod
    def printme():
        v = vars(config)
        v = map(lambda p: (p[0], p[1]), v.items())
        v = filter(lambda p: not p[0][0] == '_' and type(p[1]) != staticmethod, v)

        print('CONFIGS:')
        for (name, val) in v:
            print('\t', name, '=', val)

