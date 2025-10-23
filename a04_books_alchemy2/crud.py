from sqlalchemy.orm import Session
from models import Book,Author
class BookRepository:
    def __init__(self, session: Session):
        self.session = session    

    def create_book(self, book: Book) -> Book:
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book)  # Optional: um ID usw. zu aktualisieren
        return book


    def get_all_books(self)->list[Book]:
        return self.session.query(Book).all()
    
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
    
class AuthorRepository: # Optional
    # erstmal eine methode
    def __init__(self, session: Session):
        self.session = session

    def create_author(self, author: Author) -> Author:
        self.session.add(author)
        self.session.commit()
        self.session.refresh(author)  # Optional: um ID usw. zu aktualisieren
        return author
    
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