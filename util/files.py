#!/usr/bin/env python

import os
import re
import platform
from PySide.QtGui import QDesktopServices
import u1db
from indexer.hamsterindex import HamsterIndex
from subprocess import Popen

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

def write_m3u(media_files, output_file):
    with open(output_file, "a") as m3u_file:
        for f in media_files:
            m3u_file.write(f + "\r\n")

def os_open_file(full_file_path):
    os_type = platform.system()
    if os_type == 'Linux':
        cmd = 'xdg-open'
    elif os_type == 'Windows':
        cmd = 'start'
    elif os_type == 'Darwin':
        cmd = 'open'
    if cmd:
        print "opening %s with %s" % (full_file_path, cmd)
        Popen([cmd, full_file_path])
        return
    print "no suitible command to open file on system found"

def get_user_index():
    hamster_dir = _get_hamster_dir()
    idx_dir = os.path.join(hamster_dir, "hamster.idx")
    idx = HamsterIndex(idx_dir)
    return idx

def get_user_db():
    hamster_dir = _get_hamster_dir()
    db_file = os.path.join(hamster_dir, "hamster.db")
    db = u1db.open(db_file, create=True)
    return db

def _get_hamster_dir():
    hamster_dir = QDesktopServices.storageLocation(QDesktopServices.DataLocation)
    if not os.path.exists(hamster_dir):
        os.makedirs(hamster_dir)
        #TODO catch exception
    return hamster_dir

if __name__ == "__main__":
    import sys
    files = get_movie_files(sys.argv[1])
    write_m3u(files, "/tmp/outfile.m3u")
    os_open_file("/tmp/outfile.m3u")
