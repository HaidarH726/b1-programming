class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):

        return f"Hello, my name is {self.name} im {self.age} years old"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        student_id = int(student_id)
        self.student_id = student_id

    def introduce(self):
        return f"Hello, my name is {self.name} im {self.age} years old and my student number is {self.student_id} "


class Teacher(Person):
    def __init__(self, name, age, teacher_id, teacher_subject):
        super().__init__(name, age)
        teacher_id = int(teacher_id)
        self.teacher_id = teacher_id
        self.teacher_subject = teacher_subject


    def introduce(self):
        return f"Hello, my name is {self.name} im {self.age} years , my ID is {self.teacher_id} and I teach {self.teacher_subject} "

#test
teacher = Teacher("Kai cui", "40", 189324 , teacher_subject= "Programming")
student = Student("Haidar", "19", 248281)

print("===SCHOOL MANAGEMENT SYSTEM===")

print(teacher.introduce())
print(student.introduce())
print(f"\nStudent age: {student.age}")
print(f"Teacher subject: {teacher.teacher_subject}")


