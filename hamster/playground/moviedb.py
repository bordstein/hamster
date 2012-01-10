import couchdb

class MovieDB(object):
    def __init__(self, dbname):
        couch = couchdb.Server()
        self.db = couch[dbname]

    def get_movie(self, id):
        return self.db.get(id)

    def get_movie_id_title_for_position(self, position):
        vr = self.db.view("_design/test/_view/title", skip=position, limit=1)
        result = vr.rows[0]
        return (result.id, result.key)

    def get_movie_titles(self, startkey=None):
        if startkey:
            rv = self.db.view("_design/test/_view/title",
                    startkey=startkey)#, endkey=startkey + "\u9999")
        else:
            rv = self.db.view("_design/test/_view/title")
        return rv

    def get_total_movies(self):
        vr = self.db.view("_design/mv/_view/count")
        return vr.rows[0].value
