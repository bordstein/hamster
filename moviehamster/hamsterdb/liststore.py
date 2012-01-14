from movielist import MovieList, movielist_from_json

class ListStore(object):
    def __init__(self, u1db, username):
        self.db = u1db
        self._create_index()
        self.username = username

    def _create_index(self):
        pass

    def create(self, name):
        ml = MovieList(self.username, name)
        self.db.create_doc(ml._to_json(), ml.name())

    def save(self, movielist):
        pass

    def get(self, name):
        doc = self.db.get_doc(name)

    def get_user_list(self, name):
        doc = self.db.get_doc("%s:%s" % (self.username, name))
        if doc:
            ml = movielist_from_json(doc.content)
            return ml

if __name__ == "__main__":
    import u1db
    db = u1db.open("/tmp/list.db", create=True)
    ls = ListStore(db, "user")
    #ls.create("watched")
    print ls.get_user_list("watched")
