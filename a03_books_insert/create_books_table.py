from db_connect import connect_db
def create_books_table():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        q = '''
        CREATE TABLE IF NOT EXISTS `books` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `title` varchar(255) DEFAULT NULL,
        `author` varchar(255) DEFAULT NULL,
        `genre` varchar(100) DEFAULT NULL,
        `published_year` int(11) DEFAULT NULL,
        PRIMARY KEY (`id`)
        )'''
        cursor.execute(q)
        conn.commit()
        cursor.close()
    except Exception as e:
        print(f'Error:{e} ')