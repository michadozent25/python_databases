# A04 Books-Alchemy
## Aufgabe 
* Entwickle eine Book-Datenbank (Table:books) mit alchemy
* Datenbank:db_python06
## Dateien/Module/Klassen
* models.py -> Klasse: Book(id,isbn,title,author)
* database.oy -> Session-Konfiguration
* crud.py -> Klasse: BookRepository(Session) -> def __init__(self, session:Session)
    * Methoden (1.Version):create_book, get_all
    * Methoden (später):delete_by_isbn, update_book(Book),get_by_author, get_by_title
* main.py (optional)
## Test
* Teste die Methoden der Klasse BookRepository mit pytest 
* Ordner: tests
* pytest.ini
