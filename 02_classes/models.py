class Person:

    def __init__(self,id:int , name:str, email:str =None ):  # Person(2,'Max')
        self._id = id
        self._name = name
        self._email = email


    def __repr__(self): # Representaion für Objekt -> p = Person(2,"Max") -> print(p)
        return f"Person(id={self._id},name={self._name},email={self._email} )"
    
 
    @property # 
    def id(self):
        return self._id
    @id.setter#  p.id =3
    def id(self,id):
        self._id = id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name;

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email):
        self._email = email;

class User(Person):# User()
    pass
    #def __init__(self,id:int , name:str, email:str =None,...  ): 
    # super().__init__(id,nam,email)