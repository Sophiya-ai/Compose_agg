class Teacher():
    def teach(self):
        print("Teacher is teachinhg")
        
class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher
    def start_less(self):
        self.teacher.teach()
my_teacher = Teacher()
my_school = School(my_teacher)