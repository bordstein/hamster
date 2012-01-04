'''{
   "_id": "_design/test",
   "language": "javascript",
   "views": {
	   "title": {
		   "map": "function(doc) { emit(doc.title) }"
	   },
	   "actor": {
		   "map": "function(doc) { for (var idx in doc.cast){ emit(doc.cast[idx].name) }}"
	   },
	   "all_title": {
		   "map": "function(doc) { var tokens; if (doc.title) { tokens = doc.title.split(/[^A-Z0-9_]+/i); tokens.map(function(token) { emit(token, doc); }); }}"
		}
	}
}'''
