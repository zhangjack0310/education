from .models import StudentInfo
from models.models import Mysql

class StudentService():
    @staticmethod
    def insert_student_info(student_info):
        new_student = StudentInfo(**student_info)
        Mysql.save(new_student)
