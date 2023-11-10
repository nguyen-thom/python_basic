from student import Student
class ClassRoom:
    def __init__(self,class_name, students):
        self.class_name = class_name
        self.students = students

    def showStudents(self):
        for i in self.students:
            i.show()

    def addStudent(self, student):
        self.students.append(student)

    def removeStudent(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                return True

        return False


        #kiem tra hoc sinh "student name" co trong room khong.
        # neu co remove di va tra ve 1
        # neu khong bo qua va tra ve 0

    def searchStudent(self,student_id):
        pass
        # kiem tra hoc sinh "student id" co trong room khong.

jimmy = Student(123,"Jimmy")
tony  = Student(124, "Tony")

b2 = ClassRoom("12B2",[jimmy, tony])
b2.showStudents()

val1 = b2.removeStudent(124)
b2.showStudents()


