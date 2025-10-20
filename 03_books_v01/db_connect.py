import mysql.connector

def connect_db():
    try:
        con = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="db_python03"
        )
        return con
    except Exception as e:
        print(f"Error: {e}")
    