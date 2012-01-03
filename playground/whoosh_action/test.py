import os.path
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from schema import MySchema

if not os.path.exists("index"):
    os.mkdir("index")
    ix = create_in("index", MySchema)

ix = open_dir("index")

def store():
    writer = ix.writer()
    writer.add_document(title=u"My document", content=u"This is my document!",
                        path=u"/a", tags=u"first short", icon=u"/icons/star.png")
    writer.add_document(title=u"Second try", content=u"This is the second example.",
                        path=u"/b", tags=u"second short", icon=u"/icons/sheep.png")
    writer.add_document(title=u"Third time's the charm", content=u"Examples are many.",
                        path=u"/c", tags=u"short", icon=u"/icons/book.png")
    writer.add_document(title=u"fluppi", content=u"my?",
                        path=u"hui", tags=u"short", icon=u"/icons/book.png")
    writer.commit()


def search():
    querystring = u"my"
    parser = QueryParser("content", ix.schema)
    myquery = parser.parse(querystring)

    with ix.searcher() as searcher:
        results = searcher.search(myquery)
        print(len(results))
        for result in results:
            print(result)

if __name__ == "__main__":
    store()
    search()
