from whoosh.fields import SchemaClass, TEXT, KEYWORD, ID, STORED

class MySchema(SchemaClass):
    path = ID(stored=True)
    title = TEXT(stored=True)
    content = TEXT
    tags = KEYWORD
    icon = TEXT
