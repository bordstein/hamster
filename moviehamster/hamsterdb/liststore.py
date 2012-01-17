from movielist import MovieList, movielist_from_doc
from PySide.QtCore import QObject
import moviehamster.log as L

class ListStore(QObject):
    def __init__(self, u1db, username, parent=None):
        QObject.__init__(self, parent)
        self.db = u1db
        self._create_index()
        self.username = username

    def _create_index(self):
        indexes = self.db.list_indexes()
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

    def create(self, name, user=None):
        if not user:
            user = self.username
        ml = MovieList(user, name)
        self.db.create_doc(ml._to_json(), ml.name())

    def save(self, ml):
        if ml._doc:
            self.db.put_doc(ml._to_doc())
        else:
            raise Exception("no _doc - did you try to save new movielist?")

    def get_list(self, user, name, failsave=False):
        listname = "%s:%s" % (user, name)
        doc = self.db.get_doc(listname)
        if doc:
            ml = movielist_from_doc(doc)
            return ml
        elif failsave:
            self.create(name, user)
            return self.get_list(user, name, failsave=False)

    def get_user_list(self, name, failsave=False):
        listname = "%s:%s" % (self.username, name)
        doc = self.db.get_doc(listname)
        if doc:
            ml = movielist_from_doc(doc)
            return ml
        elif failsave:
            self.create(name)
            return self.get_user_list(listname, failsave=False)

    def get_favourites(self):
        return self.get_user_list("favourites", failsave=True)

    def get_watchlater(self):
        return self.get_user_list("watchlater", failsave=True)

    def toggle_movie_in_list(self, toggled, current_movie=None,
            name_movielist=None):
        if not current_movie:
            current_movie = self._current_movie
        if current_movie:
            if not name_movielist:
                name_movielist = self.sender()._movielist
            movielist = self.get_user_list(name_movielist, failsave=True)
            L.d("setting favourite status for %s to %s" % (current_movie, toggled))
            if toggled:
                movielist.append(current_movie)
                self.save(movielist)
            else:
                movielist.remove(current_movie)
                self.save(movielist)

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
    lm = ls.get_list("user2", "sdf", failsave=True)
