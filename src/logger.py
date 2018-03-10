
import sys

class log:
    @staticmethod
    def __prefix(l):
        return l.get_pos_string() + ' >'
    @staticmethod
    def warning(l, msg, reason):
        if not reason is None:
            if reason.startswith("LOG$"): reason = reason[4:]
            reason = 'Reason=' + reason
        print(log.__prefix(l), msg, reason, file=sys.stdout)

    @staticmethod
    def skip_include(l, path, reason):
        msg = 'skip include of \"{}\"'.format(path)
        log.warning(l, msg, reason)