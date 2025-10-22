import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crud import BookRepository
from models import Book,Base

#------------



DATABASE_URL ="sqlite:///:memory:"
#DATABASE_URL="mysql+pymysql://root:@localhost:3306/db_python06"

@pytest.fixture
def session():# TODO Parameter
    engine = create_engine(DATABASE_URL, echo=False) # create if not exists - ORM-Klassen
    Base.metadata.create_all(engine)#alle Tabellen erzeugen
    TestSession = sessionmaker(bind=engine,autoflush=False)
    session = TestSession()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)
        engine.dispose() # DB-Verbindung beenden
@pytest.fixture
def repo(session):
    return BookRepository(session)


def test_update_book_success(repo, session, sample_book):
    # Arrange
    updated_data = Book(id=sample_book.id, isbn="9876543210000", title="New Title", author="New Author")

    # Act
    updated_book = repo.update_book(updated_data)

    # Assert
    assert updated_book is not None
    assert updated_book.id == sample_book.id
    assert updated_book.title == "New Title"
    assert updated_book.author == "New Author"
    assert updated_book.isbn == "9876543210000"