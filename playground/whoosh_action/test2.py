import os.path
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from schema import MovieSchema
from normalize import get_movie_repr

if not os.path.exists("index"):
    os.mkdir("index")
    ix = create_in("index", MovieSchema)

ix = open_dir("index")

def store():
    content = get_movie_repr()
    print content
    writer = ix.writer()
    writer.add_document(title=u"the movie", content=content,
                        imdb_id=u"2")
    writer.commit()


def search():
    querystring = u"title:movie hours"
    parser = QueryParser("content", ix.schema)
    myquery = parser.parse(querystring)

    with ix.searcher() as searcher:
        results = searcher.search(myquery)
        print(len(results))
        for result in results:
            print(result)

if __name__ == "__main__":
    #store()
    search()
