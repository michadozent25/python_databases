import mysql.connector

try:
    con = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="db_python02"
    )
    print("Autocommit: ",con.autocommit)
    cursor = con.cursor()

    q = ''' CREATE TABLE IF NOT EXISTS  user( 
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        email VARCHAR(50) 
    )

    ''' 
    cursor.execute(q)

    # Speichern - Insert
    insert_query ="INSERT INTO user (name,email) VALUES (%s,%s)"
    cursor.execute(insert_query, ("Otto","otto@web.de"))
    con.commit()


    # Lesen -Select

    select_query = "SELECT * FROM user"
    cursor.execute(select_query)
    for row in cursor.fetchall():
        print(row)


    cursor.close()
    con.close()
except Exception as e:
    print(f"Error {e}")