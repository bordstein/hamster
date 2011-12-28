import imdb
import u1db
import json

def fetch_movie(imdb_id):
    ia = imdb.IMDb()
    movie = ia.get_movie(imdb_id)
    movie_dict = {}
    movie_dict["title"] = movie['title']
    movie_dict["year"] = movie['year']
    return json.dumps(movie_dict)

if __name__ == "__main__":
    imdb_id = '1120985'
    #movie = fetch_movie(imdb_id)
    db = u1db.open("/tmp/my.db", create=True)
    #doc = db.create_doc(movie, imdb_id)

    #querying
    #db.create_index('by_title', ['title'])
    results = db.get_from_index(
            'by_title', [
                ("Blue*", )
                ])
    for result in results:
        print result.doc_id
        print result.content
