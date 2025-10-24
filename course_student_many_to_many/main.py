from database import Base, engine, session
from models import Student
from crud import StudentRepository,CourseRepository
def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)# create table if not exists
    studentrepo = StudentRepository(session)
    courserepo = CourseRepository(session)
    
    studentrepo.add_student("Ina")
    courserepo.add_course("Python")

   
if __name__=="__main__":
    main()
