#!/usr/bin/env python

from gevent import monkey; monkey.patch_socket()
from dbcloner import normalize

import os
import re
import imdb
import json
#import u1db
import couchdb
import gevent
from gevent import pool
from whoosh_action.index import HamsterIndex

rex = re.compile(".*\[(\d{7})\]")
imdb_db = imdb.IMDb()
index = HamsterIndex("/tmp/hamster.idx")
#db = u1db.open("/tmp/out.db", create=True)
couch = couchdb.Server()
db = couch['movies']

g_pool = pool.Pool(size=25)
global count
count = 0

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
    #db.create_doc(json.dumps(nm), doc_id=imdb_id)
    nm['_id'] = str(imdb_id)
    #db.save(nm)
    index.index_movie(nm)
    print "fetched!"

def counter(arg, directory, files):
    global count
    for file in files:
        match = rex.match(file)
        if match:
            count+=1

os.path.walk("/media/DATA/media/movies/", callback, "secret message")
#os.path.walk("/media/DATA/media/movies/", counter, "secret message")
#print count
