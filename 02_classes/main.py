from models import Person

def main():
    p1 = Person(1,"Ina","ina@web.de")
    p2 = Person(2,"Max") 
    print(p1,p2)

    p1.name = "Anna"
    print(p1,p2)

    print(p1.id)
if __name__ =="__main__":
    main()