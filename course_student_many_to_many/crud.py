from models import Student, Course

class StudentRepository:
    def __init__(self,session):
        self.session =session


    def add_student(self,name:str):
        student = Student(name=name)
        self.session.add(student)
        self.session.commit()
        return student
class CourseRepository:
    def __init__(self,session):
        self.session =session
    def add_courset(self,name:str):
        course = Course(name=name)
        self.session.add(course)
        self.session.commit()
        return course