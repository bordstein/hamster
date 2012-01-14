from movielist import MovieList, movielist_from_doc

class ListStore(object):
    def __init__(self, u1db, username):
        self.db = u1db
        self._create_index()
        self.username = username

    def _create_index(self):
        indexes = db.list_indexes()
        if "by-name" not in [idx[0] for idx in indexes]:
            self.db.create_index("by-name", ['name'])
        if "userlists-by-name" not in [idx[0] for idx in indexes]:
            self.db.create_index("userlists-by-name", ['user', 'name'])

    def list_user_lists(self):
        results = self.db.get_from_index(
        "userlists-by-name",             # name of index
            [                            # begin the list of index keys
                (self.username, "*", )   # an index key
            ]
        )
        return _extract_doc_ids(results)

    def list_all_lists(self):
        results = self.db.get_from_index(
        "by-name",                     # name of index
            [                               # begin the list of index keys
                ("*", )                  # an index key
            ]
        )
        return _extract_doc_ids(results)

    def create(self, listname):
        ml = MovieList(self.username, listname)
        self.db.create_doc(ml._to_json(), ml.name())

    def save(self, ml):
        if ml._doc:
            db.put_doc(ml._to_doc())
        else:
            raise Exception("no _doc - did you try to save new movielist?")

    def get(self, name):
        doc = self.db.get_doc(name)

    def get_user_list(self, name):
        doc = self.db.get_doc("%s:%s" % (self.username, name))
        if doc:
            ml = movielist_from_doc(doc)
            return ml

def _extract_doc_ids(doclist):
    retval = []
    for doc in doclist:
        retval.append(doc.doc_id)
    return retval

if __name__ == "__main__":
    import u1db
    db = u1db.open("/tmp/list.db", create=True)
    ls = ListStore(db, "user")
    #ls.create('blupp')
    #ml = ls.get_user_list("watched")
    #ml.append(2323)
    #ls.save(ml)
    #print ml
    print ls.list_user_lists()
    print ls.list_all_lists()
