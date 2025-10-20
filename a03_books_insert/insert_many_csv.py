import csv
import os
def create_books(csv_file:str):
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir,'books.csv')

    tupel_list = []
    with open(full_path,newline='',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tupel_list.append((row['id'], row['title'],row['author'],row['genre'],row['published_year']))
    return tupel_list


def insert_books(conn,tuple_list):
    cursor = conn.cursor()
    sql = "INSERT INTO books(id, title, author, genre, published_year)VALUES(%s,%s,%s,%s,%s)"
    cursor.executemany(sql, tuple_list)
    conn.commit()