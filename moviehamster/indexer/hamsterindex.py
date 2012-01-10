#!/usr/bin/env python

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

import os
from whoosh.qparser import QueryParser
from whoosh.index import create_in, open_dir
from schema import MovieSchema

class HamsterIndex(object):
    def __init__(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
            self.index = create_in(path, MovieSchema)

        self.index = open_dir(path)
        self.q_parser = QueryParser("title", self.index.schema)

    def index_movie(self, movie):
        u = unicode
        cast = movie["cast"]
        actors = [c['name'] for c in cast]
        director = movie["director"]
        directors = [c['name'] for c in cast]

        writer = self.index.writer()
        writer.add_document(
                imdb_id=u(movie["_id"]),
                title=u(movie["title"]),
                genre= u(";".join(movie["genres"])),
                plot=u(movie.get("plot", "")),
                cast=u(";".join(actors)),
                director=u(";".join(directors)),
                rating=movie["rating"]
                )
        writer.commit()

    def list_all(self):
        num = 0
        retval = []
        with self.index.searcher() as searcher:
            for res in searcher.reader().all_stored_fields():
                num += 1
                retval.append(res)
        return retval

    def query(self, querystring):
        querystring = unicode(querystring)
        myquery = self.q_parser.parse(querystring)

        with self.index.searcher() as searcher:
            results = searcher.search(myquery)
            retval = []
            for res in results:
                retval.append(res.fields())
            return retval


if __name__ == "__main__":
    import sys
    from moviehamster.util.files import get_user_index
    idx = get_user_index()
    idx.list_all()
    query = sys.argv[1]
    print "query:", query
    results = idx.query(query)
    print len(results)
    for res in results:
        print res
