class Student:
    def __init__(self, name, surname, student_id):
        self.name=name
        self.surname=surname
        self.student_id=student_id
        self.grades=[] #пустой список grades для хранения оценок студента

    def __str__(self):
        return f"Student(name='{self.name}', surname='{self.surname}', student_id={self.student_id}, grades={self.grades})"

    def __eq__(self, other): #проверка на равенство
        if isinstance(other, Student): # проверка, является ли other объектом класса Student.
            return self.student_id==other.student_id
        return False

    def __len__(self): # количество оценок
        return len(self.grades)

student1 = Student('Полина', 'Краснова', 8)
student1.grades = [5, 4, 5, 4]

student2 = Student('Татьяна', 'Савельева', 8)
student2.grades = [5, 5, 4, 4]

print(student1)  # вызов __str__ 
print(student1 == student2)  # вызов __eq__ (True, так как student_id совпадает)
print(len(student1))  # вызов __len__ (кол-во оценок)
