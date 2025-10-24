from sqlalchemy.orm import Session
from models import Book,Author
from typing import  Generic,  TypeVar, Type
from sqlalchemy import select
T = TypeVar("T")

class BaseRepository(Generic[T]):
    """Generisches Repo für einfache CRUD-Operationen."""
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

  # ---------- Create ----------
    def create(self, obj: T) -> T:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj
    def list_all(self) -> list[T]:
        return list(self.session.scalars(select(self.model)))
    # find_by_id, delete_by_id, 
class BookRepository(BaseRepository[Book]):
    def __init__(self, session: Session):
        super().__init__(session, Book)
 

    def create_book(self, book: Book) -> Book:
       return super().create(book)


    def get_all_books(self)->list[Book]:
        return super().list_all()
    
    def get_book_by_id(self,id:int)->Book|None:
        return self.session.query(Book).filter(Book.id==id).first()
    
    def update_book(self, book: Book) -> Book | None:
        db_book = self.get_book_by_id(book.id)
        if not db_book:
            return None

        # Felder aktualisieren
        if book.title:
            db_book.title = book.title
        if book.author:
            db_book.author = book.author
        if book.isbn:
            db_book.isbn = book.isbn

        self.session.commit()
        self.session.refresh(db_book)
        return db_book

    def delete_book_by_id(self, id: int) -> Book | None:
        book = self.get_book_by_id(id)
        if book:
            self.session.delete(book)
            self.session.commit()
        return book
    def add_author(self, author: Author, book_id: int) -> Author:
        book = self.get_book_by_id(book_id)
        if book:
            book.authors.append(author)
            self.session.commit()
        return author
    
class AuthorRepository(BaseRepository[Author]): 
    # erstmal eine methode
    def __init__(self, session: Session):
        super().__init__(session, Author)


    def create_author(self, author: Author) -> Author:
        return super().create(author)
    
    def add_author_to_book(self, author_id: int, book_id: int) -> Author | None:
        """Verknüpft einen vorhandenen Autor mit einem vorhandenen Buch."""
        author = self.session.query(Author).filter(Author.id == author_id).first()
        book = self.session.query(Book).filter(Book.id == book_id).first()
        
        if not author or not book:
            return None

        book.authors.append(author)
        self.session.commit()
        self.session.refresh(author)
        return author