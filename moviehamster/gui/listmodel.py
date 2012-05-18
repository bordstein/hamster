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

from resmodel import GenericListModel
import moviehamster.log as L
 
class ListModel(GenericListModel): 
    def __init__(self, hamsterdb, list_to_display, liststore, parent=None):
        GenericListModel.__init__(self, list_to_display, liststore, parent)
        self.movie_list = list_to_display
        self.db = hamsterdb
        self.cache = {}
 
    def getIdForRow(self, row):
        return self.movie_list[row]

    def getData(self, row, key):
        imdb_id = self.movie_list[row]
        search_result = self.cache.get(imdb_id, self.db.search(imdb_id))
        if not search_result:
            L.e("could not find movie by id")
            return ""
        self.cache[imdb_id] = search_result[0]
        return search_result[0][key]
