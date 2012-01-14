import json
from copy import deepcopy

class MovieList(list):
    def __init__(self, username, listname):
        self.user = username
        self.listname = listname

    def name(self):
        return "%s:%s" % (self.user, self.listname)

    def _to_json(self):
        json_obj = {}
        json_obj['user'] = self.user
        json_obj['name'] = self.listname
        json_obj['hamster-type'] = "list"
        json_obj['content'] = self
        return json.dumps(json_obj)

    def _to_doc(self):
        doc = deepcopy(self._doc)
        doc.content = self._to_json()
        return doc

def movielist_from_json(json_string):
    loaded_obj = json.loads(json_string)
    ml = MovieList(loaded_obj["user"], loaded_obj['name'])
    ml.extend(loaded_obj["content"])
    return ml

def movielist_from_doc(doc):
    ml = movielist_from_json(doc.content)
    doc.content = None
    ml._doc = doc
    return ml


if __name__ == "__main__":
    l = MovieList('hans', 'huber')
    l.append('23')
    json_string = l._to_json()
    print json_string
    l2 = movielist_from_json(json_string)
    print l2
    json_string = l2._to_json()
    print json_string
