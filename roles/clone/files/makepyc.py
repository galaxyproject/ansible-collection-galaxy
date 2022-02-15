#!/usr/bin/env python3

import compileall
import sys

from os import unlink, removedirs, walk
from os.path import dirname, exists, join


assert sys.argv[1], "usage: makepyc /path/to/lib"


pyc_ext = '.cpython-' + ''.join(map(str, sys.version_info[:2])) + '.pyc'
pyc_ext_len = len(pyc_ext)


for root, dirs, files in walk(sys.argv[1]):
    parent = dirname(root)
    for name in files:
        if name.endswith(pyc_ext):
            pyc = join(root, name)
            py = join(parent, name[:-pyc_ext_len] + '.py')
            if not exists(py):
                print(f"Removing orphaned bytecode '{pyc}'...")
                unlink(pyc)
    try:
        # this will fail a lot, safe to ignore
        removedirs(root)
        print(f"Removed empty directory '{root}'...")
    except:
        pass

compileall.compile_dir(sys.argv[1])
