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
    idx = HamsterIndex("/tmp/hamster.idx")
    results = idx.query("cast:DiCaprio cast:Nicholson")
    print len(results)
    for res in results:
        print res
