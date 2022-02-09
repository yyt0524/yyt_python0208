import os
import sys

def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

#for i in sys.argv[1:]:
print(get_suffix(sys.argv[1]))


os.system('pause')