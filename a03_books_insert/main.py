from create_books_table import create_books_table
from db_connect import connect_db   
from insert_many_csv import insert_books, create_books

def main():
    create_books_table()
    insert_books(connect_db(),create_books('books.csv'))
if __name__=="__main__":
    main()