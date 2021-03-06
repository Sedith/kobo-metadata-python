#!/usr/bin/python3
import re
from os import listdir
from os.path import isfile, isdir, join


def sorted_aphanumeric(path, ext=[], ignore=[], dirs=False):
    """Alphanumeric sort all files in path.
    Only consider extensions in ext, ignore filenames in ignore, and list only directions if dirs.
    """
    data = [
        f
        for f in listdir(path)
        if (
            ((not dirs and isfile(join(path, f))) or (dirs and isdir(join(path, f)))) and f not in ignore and (ext == [] or get_ext(f.lower()) in ext)
        )
    ]
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


def get_ext(file):
    """Return the extension of the given filename."""
    return file.split('.')[-1]
