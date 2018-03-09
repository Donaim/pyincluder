
import os

class outer(object):
    def __init__(self, out_path: str):
        self.out_path = out_path
        self.out = open(self.out_path, 'w+', encoding='utf-8')
    def write(self, text: str):
        self.out.write(text)

    def close(self):
        self.out.close()
    