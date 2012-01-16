#!/usr/bin/env python

#############################################################################
##  Hamster - Nice and friendly movie collection manager
##  Copyright (C) 2012 Christoph Meinhart, Michael Seiwald
##  
##  This file is part of Hamster.
##  
##  Hamster is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 2 of the License, or
##  (at your option) any later version.
##  
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##  
##  You should have received a copy of the GNU General Public License along
##  with this program; if not, write to the Free Software Foundation, Inc.,
##  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
## 
#############################################################################

import imdb
from numbers import Number
import base64
import urllib

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
        pers = {}
        pers['name'] = obj['name']
        pers['person_id'] = "person_%s" % obj.getID()
        if isinstance(obj.currentRole, imdb.Character.Character):
            if 'name' in obj.currentRole.keys():
                pers['role'] = obj.currentRole['name']
        elif isinstance(obj.currentRole, imdb.utils.RolesList):
            tmpList = []
            for role in obj.currentRole:
                if 'name' in role.keys():
                    tmpList.append(role['name'])
            pers['role'] = tmpList
        return pers
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

def convert_person(imdb_person):
    person = {}
    person['name'] = imdb_person['name']
    try:
        person['mini biography'] = imdb_person['mini biography'][0]
    except:
        person['mini biography'] = 'No biography available'
    person['actor'] = _get_movie_ids_for_person(imdb_person, "actor")
    person['director'] = _get_movie_ids_for_person(imdb_person, "director")
    person['producer'] = _get_movie_ids_for_person(imdb_person, "producer")
    headshot_url = imdb_person.get('headshot', None)
    if headshot_url:
        person['headshot'] = base64.b64encode(urllib.urlopen(imdb_person['headshot']).read())
    else:
        person['headshot'] = '-'
    return person

def _get_movie_ids_for_person(imdb_person, role):
    tmp_list = []
    for movie in imdb_person.get(role, []):
        tmp_list.append(movie.getID())
    return tmp_list
