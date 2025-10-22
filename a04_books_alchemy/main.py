from database import session, Base, engine
from models import Book
from crud import BookRepository


def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    repo =  BookRepository(session)
    newBook = Book(isbn="983-32-23323-23-3",title="Clean Code", author="Robert C. Martin")
    created = repo.create_book(newBook)
    print(created)

if __name__=="__main__":
    main()