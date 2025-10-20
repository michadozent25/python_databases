from models import Book
from mysql.connector.connection import MySQLConnection
class BookRepository:
    ''' alle Datenbank-Zigriffsmethode für Books '''
    def __init__(self,conn:MySQLConnection):
        self.conn = conn
    


    def save(self, book:Book) ->Book:
        #TODO Fehlerprüfung
        cursor = self.conn.cursor()
        sql = '''
            INSERT INTO books (title, author, genre, published_year) values (%s,%s,%s,%s)
            '''
        values = (book.title, book.author, book.genre, book.published_year)
        cursor.execute(sql,values)
        self.conn.commit()
        book.id = cursor.lastrowid
        cursor.close()
        return book
    
    def find_all(self)->list[Book]:
        cursor = self.conn.cursor(dictionary=True)
        sql="SELECT * FROM books"
        cursor.execute(sql)
        # result = []
        # for row  in cursor.fetchall():
        #     # TODO mit Kurzform verbessern!!!
        #     result.append(Book(id=row[0],title=row[1],author=row[2],genre=row[3],published_year=row[4]))
        result = cursor.fetchall()
        return [Book(**row)  for row in result]# Liste aus Dictionaries zu Liste mit Book-Objekten
    
    def delete_by_id(self,id:int)->bool:
        cursor = self.conn.cursor()
        sql ="DELETE FROM books WHERE id =%s"
        cursor.execute(sql,(id,))
        self.conn.commit()
        del_rows = cursor.rowcount
        return del_rows == 1
    
    def find_by_author(self,author:str)->list[Book]:
        pass

    def count_books(self)->int:
        cursor = self.conn.cursor()
        try:
            sql = "SELECT count(*) FROM books"
            cursor.execute(sql)
            (count,) = cursor.fetchone()
            return count
        finally:
            cursor.close()
    def update(self,book:Book)->Book:
        

        pass
