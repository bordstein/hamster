#!/usr/bin/env python
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
    idx = HamsterIndex("/media/DATA/hamster/hamster.idx")
    idx.list_all()
    query = sys.argv[1]
    print "query:", query
    results = idx.query(query)
    print len(results)
    for res in results:
        print res
