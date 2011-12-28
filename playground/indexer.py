#!/usr/bin/env python

from gevent import monkey; monkey.patch_socket()
from dbcloner import normalize

import os
import re
import imdb
import json
import u1db
import gevent
from gevent import pool

rex = re.compile(".*\[(\d{7})\]")
imdb_db = imdb.IMDb()
db = u1db.open("/tmp/out.db", create=True)

g_pool = pool.Pool(size=25)

def callback(arg, directory, files):
    for file in files:
        match = rex.match(file)
        if match:
            imdb_id = match.group(1)
            g_pool.spawn(fetch_and_normalize, imdb_id)
            gevent.sleep(0)

def fetch_and_normalize(imdb_id):
    print "fetching", imdb_id, "..."
    movie = imdb_db.get_movie(imdb_id)
    nm = normalize(movie)
    db.create_doc(json.dumps(nm), doc_id=imdb_id)
    print "fetched!"

os.path.walk("/media/DATA/media/movies/", callback, "secret message")
