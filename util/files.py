#!/usr/bin/env python
import os
import re
rex = re.compile(r".*\.(avi|mkv|mov)")

def get_movie_files(directory):
    full_path_dir = os.path.abspath(directory)
    files = os.listdir(full_path_dir)
    movie_files = []
    for f in files:
        if rex.match(f):
            full_mv_path = os.path.join(full_path_dir, f)
            movie_files.append(full_mv_path)
    return movie_files

if __name__ == "__main__":
    import sys
    print get_movie_files(sys.argv[1])
