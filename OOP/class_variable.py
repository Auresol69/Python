# class variables = Shared among all instances of a class
#                   Defined outside the constructor

class Student:

    class_year = 2024 # <-- Class variable
    num_students = 0
    students_list = [] # <-- Giống ArrayList chứa đối tượng Student

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1 # Biến class phải có TênClass.BiếnClass
        Student.students_list.append(self) # add thêm 1 đối tượng Student vào students_list

    # Tựa như toString (in ra đẹp hơn)
    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"

student1 = Student("Roy", 20)
student2 = Student("Bro_Code", 35)
student3 = Student("Spongebob", 30)
student4 = Student("Sandy", 27)

# print(Student.class_year)
# print(Student.num_students)
#
# print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
# print(student1.name)
# print(student2.name)
# print(student3.name)
# print(student4.name)

for student in Student.students_list:
    print(student)