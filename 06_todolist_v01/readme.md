# Todolist
## Version 0.1
## Model
* Todo
    * id
    * task:str
    * description:str
    * deadline:Date
    * state:(Enum("OPEN","IN_PROGRESS","DONE"))
    * optional: priority
* User
    * id
    * name
    * password



## Aufgabe
1. Konfiguration/Struktur: database.py,main, pytest.ini: Datenbank anlegen db_todo: MYSQL
2. Ergänze die Modelklassen um relationship (1:N) und ForeignKeys
3. Implementiere UserRepository, TodoRepository -> create/findAll
4. Teste mit Unittest/pytest die RepositoryMethoden (evtl. first Test)
5. evtl. Test in main

------ RepositoryMethoden-----------------
6. 
7. 

