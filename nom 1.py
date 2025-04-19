class Student:
    def __init__(self, name, student_id):
        self.name = name          # сохраняем name в текущем объекте
        self.student_id = student_id  # сохраняем student_id в текущем объекте
        self.grades = []          # создаем пустой список grades для текущего объекта

    def add_grade(self, grade): # Добавляем оценку в список оценок студента
        if 0<=grade<=10: # Проверяем, что оценка находится в допустимом диапазоне (0-10)
            self.grades.append(grade) # Добавляем длпустимую оценку
        else:
            print('Ошибка. Оценка не в диапазоне 0-10') # Если оценка вне диапазона, выводит сообщение об ошибке
            
    def get_average(self): # Вычисляем средний балл студента
        if not self.grades:
            return 0.0 # Если нет оценок, возвращаем 0.0
        return sum(self.grades)/len(self.grades) # Иначе возвращаем среднее арифметическое всех оценок
    
    def display_info(self):
        print(f'Студент: {self.name}')
        print(f'ID: {self.student_id}')
        print(f"Оценки: {', '.join(map(str,self.grades))}") # Список оценок (преобразованный в строку)
        print(f'Средний балл: {self.get_average():.2f}\n') # Средний балл (с округлением до 2 знаков после запятой)
        
if __name__=="__main__":
    student1 = Student("Краснова Полина", "202")
    student1.add_grade(3)
    student1.add_grade(8)
    student1.display_info()
