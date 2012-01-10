from whoosh.fields import SchemaClass, TEXT, KEYWORD, ID, STORED, NUMERIC, NGRAM

class MySchema(SchemaClass):
    path = ID(stored=True)
    title = TEXT(stored=True)
    content = TEXT
    tags = KEYWORD
    icon = TEXT

class MovieSchema(SchemaClass):
    imdb_id = ID(stored=True)
    title = NGRAM(stored=True)
    plot = TEXT
    cast = TEXT
    director = TEXT
    genre = KEYWORD
    rating = NUMERIC(type=float)
