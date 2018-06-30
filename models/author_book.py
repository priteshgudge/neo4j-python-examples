from neomodel import StructuredNode, StringProperty, RelationshipTo, IntegerProperty, RelationshipFrom, config
from neomodel import db
db.set_connection('bolt://neo4j:neo4j@localhost:7687')


config.DATABASE_URL = 'bolt://neo4j:neopass@localhost:7687'

class Book(StructuredNode):
    id = IntegerProperty(unique_index=True)
    title = StringProperty(unique_index=True)
    author = RelationshipTo('Author', 'AUTHOR')

class Author(StructuredNode):
    id = IntegerProperty(unique_index=True)
    name = StringProperty(unique_index=True)
    books = RelationshipFrom('Book', 'AUTHOR')

harry_potter = Book(title='Harry potter and the..',id=1).save()
rowling =  Author(name='J. K. Rowling',id=2).save()
harry_potter.author.connect(rowling)

book1 = Book.get_or_create(id=1)
print (book1)
auth1 = Author.get_or_create(id=2)
books = auth1.books
print (books)

