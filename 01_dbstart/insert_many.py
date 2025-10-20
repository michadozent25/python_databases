from db_connect import connect_db

try:
    con = connect_db()
    cursor = con.cursor() 


    data =[
        ("Anna","aa@web.de"),
        ("Max","m@web.de"),
        ("Ina","ii@web.de")
    ] 

    q = "INSERT INTO user(name,email) VALUES (%s,%s)"
    cursor.executemany(q,data)
    con.commit()
except Exception as e:
    print(f"Error: {e}")

