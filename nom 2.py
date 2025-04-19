class Person:
    def __init__(self, name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # super-вызывает объект родительского класса, избегая дублирования и ошибок
        self.student_id = student_id # Уникальный ID студента

    def __str__(self): # Возвращает строку в формате: Student(name=Имя, age=Возраст, id=ID)
        return f"Student(name={self.name}, age={self.age}, id={self.student_id})"

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age) #Вызов конструктора родителя
        self.subject=subject # добавляем предмет преподавания
        self.students=[] # создаем пустой список студентов

    def add_student(self, student): #добавляем студента в список
        if student not in self.students: # проверка на дублирование
            self.students.append(student) # добавляем в список
            print(f'Студент {student.name} добавлен к преподавателю {self.name}')
        else:
            print(f'Студент {student.name} уже есть у преподавателя {self.name}')
    
    def remove_student(self, student): #удаляем студента из списка
        if student in self.students: # проверка наличия
            self.students.remove(student) # удаляем из списка
            print(f'Студент {student.name} удален у преподавателя {self.name}')
        else:
            print(f'Студента {student.name} нет у преподавателя {self.name}')
    
    def list_students(self): #удаляем студента из списка
        print(f'\nСписок студентов преподавателя {self.name} ({self.subject}):')
        if not self.students: # проверка на пустой список
            print('нет студентов')
        else:
            for student in self.students: # перебор всех студентов
                print(f'{student.name}')

if __name__ == "__main__": #создаем студентов
    student1 = Student('Краснова Полина',18, '202')
    student2 = Student('Савельева Татьяна',19, '128')

    #создаем преподавателя
    teacher = Teacher('Ирина Николаевна', 65, 'Математика')

    #добавляем студентов
    teacher.add_student(student1)
    teacher.add_student(student2)
    teacher.add_student(student2) #попытка добавить повторно

    #выводим список
    teacher.list_students()

    #удаляем студента
    teacher.remove_student(student1)
    teacher.remove_student(student1)  #попытка удалить повторно

    #выводим обновленный список
    teacher.list_students()
