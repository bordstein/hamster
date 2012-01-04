#!/usr/bin/env python

#from gevent import monkey; monkey.patch_socket()
from dbcloner import normalize

import os
import re
import imdb
#import json
#import u1db
#import couchdb
#import gevent
#from gevent import pool
from multiprocessing import Pool
from whoosh_action.index import HamsterIndex
from indexwriter import QueueManager

def fetch_and_normalize(imdb_id):
    print "fetching", imdb_id, "..."
    imdb_db = imdb.IMDb()
    movie = imdb_db.get_movie(imdb_id)
    nm = normalize(movie)
    #db.create_doc(json.dumps(nm), doc_id=imdb_id)
    nm['_id'] = str(imdb_id)
    #db.save(nm)
    #index.index_movie(nm)
    print "fetched!"
    QueueManager.register('index')
    m = QueueManager(address=('', 50000), authkey='abracadabra')
    m.connect()
    m.index(nm)

def callback(arg, directory, files):
    for file in files:
        match = rex.match(file)
        if match:
            imdb_id = match.group(1)
            #g_pool.spawn(fetch_and_normalize, imdb_id)
            #gevent.sleep(0)
            pool.apply_async(fetch_and_normalize, (imdb_id,))

def counter(arg, directory, files):
    global count
    for file in files:
        match = rex.match(file)
        if match:
            count+=1

rex = re.compile(".*\[(\d{7})\]")
imdb_db = imdb.IMDb()
index = HamsterIndex("/tmp/hamster.idx")
#db = u1db.open("/tmp/out.db", create=True)
#couch = couchdb.Server()
#db = couch['movies']

#g_pool = pool.Pool(size=25)
pool = Pool(8)
global count
count = 0

os.path.walk("/media/DATA/media/movies/", callback, "secret message")
pool.close()
pool.join()
#os.path.walk("/media/DATA/media/movies/", counter, "secret message")
#print count
