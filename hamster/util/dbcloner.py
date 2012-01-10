#!/usr/bin/env python

import imdb
from numbers import Number

def normalize(obj):
    #print "normalizing", obj
    if isinstance(obj, basestring):
        return obj
    elif isinstance(obj, Number):
        return obj
    elif isinstance(obj, dict):
        return _dictify(obj)
    elif isinstance(obj, list):
        return _listify(obj)
    elif isinstance(obj, imdb.Movie.Movie):
        return _dictify(obj)
    elif isinstance(obj, imdb.Person.Person):
        return _dictify(obj)
    elif isinstance(obj, imdb.Company.Company):
        return _dictify(obj)
    else:
        raise BaseException("unhandled type:" + str(type(obj)))

def _listify(obj):
    new_list = []
    for entry in obj:
        new_list.append(normalize(entry))
    return new_list

def _dictify(obj):
    new_dict = {}
    for key in obj.keys():
        entry = obj[key]
        new_dict[key] = normalize(entry)
    return new_dict


if __name__ == "__main__":
    import json
    import u1db

    # fetching imdb infos
    imdb_db = imdb.IMDb()
    imdb_id = "0325980"
    movie = imdb_db.get_movie(imdb_id)

    # normalize movie
    nm = normalize(movie)

    # connect to u1db and save doc
    db = u1db.open(":memory:", create=True)
    db.create_doc(json.dumps(nm), doc_id=imdb_id)
    
    # fetch, load and print doc
    restored_doc = db.get_doc(imdb_id)
    print json.loads(restored_doc.content)
    print "\n\nok"
