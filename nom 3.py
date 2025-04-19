import math
from abc import ABC, abstractmethod # abc - используются для создания абстрактных базовых классов

class Shape(ABC): # абстрактный класс "Фигура"
    @abstractmethod # ошибка будет видна сразу при создании класса
    def area(self): #площадь
        pass
    
    @abstractmethod
    def perimeter(self): #периметр
        pass


class Rectangle(Shape): #прямоугольник
    def __init__(self, width, height):
        self.width=width  # Ширина прямоугольника
        self.height=height # Высота прямоугольника
    
    def area(self): #площадь
        return self.width * self.height #ширина*высота
    
    def perimeter(self): #периметр
        return 2*(self.width + self.height)
    
    def __str__(self): # переделывает в строку
        return f'Rectangle(width={self.width}, height={self.height})'


class Circle(Shape): # круг
    def __init__(self,radius):
        self.radius=radius
    
    def area(self): # площадь круга (пи × радиус²)
        return math.pi*self.radius**2
    
    def perimeter(self): # (длина окружности) (2 × π × радиус)
        return 2 * math.pi * self.radius
    def __str__(self): # переделывает в строку
        return f'Circle(radius={self.radius})'


class Triangle(Shape): #треугольник
    def __init__(self, side1, side2, side3): # Конструктор принимает три стороны треугольника
        self.side1=side1
        self.side2=side2
        self.side3=side3
    
    def area(self): #по формуле Герона
        s=self.perimeter()/2
        return math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3)) 
    
    def perimeter(self):
        return self.side1+self.side2+self.side3
    
    def __str__(self):
        return f'Triangle(side1={self.side1}, side2={self.side2}, side3={self.side3})'


def print_shape_info(shape):
    print(f'Фигура: {shape}')
    print(f'Площадь: {shape.area():.2f}') # Площадь с округлением до 2 знаков после запятой
    print(f'Периметр: {shape.perimeter():.2f}') # Периметр с округлением до 2 знаков после запято
    print()
# Демонстрация полиморфизма
if __name__ == "__main__":
    shapes = [
        Rectangle(3, 6), # Прямоугольник 3*6
        Circle(4), # Круг радиусом 4
        Triangle(2, 3, 4) # Треугольник со сторонами 2,3,4
    ]
    
    for shape in shapes:
        print_shape_info(shape)
















        
