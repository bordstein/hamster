#############################################################################
##  Hamster - Nice and friendly movie collection manager
##  Copyright (C) 2012 Christoph Meinhart, Michael Seiwald
##  
##  This file is part of Hamster.
##  
##  Hamster is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 2 of the License, or
##  (at your option) any later version.
##  
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##  
##  You should have received a copy of the GNU General Public License along
##  with this program; if not, write to the Free Software Foundation, Inc.,
##  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
## 
#############################################################################


import u1db
import json
from imdb import IMDb
import os
from whoosh.qparser import QueryParser
from whoosh.index import create_in, open_dir
from schema import MovieSchema
from util import normalize

class HamsterDB(object):
    def __init__(self, index_path, db_path):
        self._setup_whoosh_index(index_path)
        self._setup_u1db(db_path)
        self.imdb = IMDb()

    def _setup_u1db(self, db_path):
        self.db = u1db.open(db_path, create=True)

    def _setup_whoosh_index(self, index_path):
        if not os.path.exists(index_path):
            os.mkdir(index_path)
            self.index = create_in(index_path, MovieSchema)

        self.index = open_dir(index_path)
        self.q_parser = QueryParser("title", self.index.schema)

    def _fetch_u1db_movie(self, imdb_id):
        doc = self.db.get_doc(imdb_id)
        if doc:
            return json.loads(doc.content)

    def get_movie(self, imdb_id):
        movie = self._fetch_u1db_movie(imdb_id)
        if not movie:
            # not in local db, fetch from imdb
            imdb_movie = self.imdb.get_movie(imdb_id)
            movie = normalize(imdb_movie)
            self.db.create_doc(json.dumps(movie), doc_id=imdb_id)
            self._index_movie(imdb_id, movie)
        return movie
    
    def _index_movie(self, imdb_id, movie):
        u = unicode
        cast = movie["cast"]
        actors = [c['name'] for c in cast]
        director = movie["director"]
        directors = [c['name'] for c in cast]

        writer = self.index.writer()
        writer.add_document(
                imdb_id=u(imdb_id),
                title=u(movie["title"]),
                year=movie["year"],
                genre= u(";".join(movie["genres"])),
                cast=u(";".join(actors)),
                director=u(";".join(directors)),
                rating=movie["rating"]
                )
        writer.commit()

    def get_person(self, imdb_id):
        pass

    def search(self, query):
        pass

if __name__ == "__main__":
    db = HamsterDB("/tmp/hamster.idx", "/tmp/hamster.db")
    movie = db.get_movie("0325980")
    print movie['title']
