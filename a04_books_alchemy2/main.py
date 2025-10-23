from database import session, Base, engine
from models import Book,Author
from crud import BookRepository,AuthorRepository


def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    bookrepo =  BookRepository(session)
    authorrepo = AuthorRepository(session)
    book = Book(isbn="978-3-16-148410-0", title="Das Buch der Bücher")
    author1 = Author(name="Alice", book=book)
    author2 = Author(name="Bob", book=book)

    bookrepo.create_book(book)
    authorrepo.add_author_to_book(author1.id, book.id)
    authorrepo.add_author_to_book(author2.id, book.id)

    print(bookrepo.get_all_books())

   
  



if __name__=="__main__":
    main()