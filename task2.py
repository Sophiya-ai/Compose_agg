# Продемонстрировать принцип полиморфизма через реализацию разных классов,
# представляющих геометрические формы, и метод для расчёта площади каждой формы.
# Создать базовый класс Shape с методом area(), который просто возвращает 0.
# Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square),
# каждый из которых переопределяет метод area().
# В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
# Написать функцию, которая принимает объект класса Shape и выводит его площадь.
class Shape():
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self,R):
        self.R = R
    def area(self):
        return 3.14*self.R**2
class Rectangle(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a*self.b
class Square(Shape):
    def __init__(self,a):
        self.a = a
    def area(self):
        return self.a**2
def print_area(shape):
    print(f"Площадь - {shape.area()}")
cir = Circle(5)
rec = Rectangle(3,4)
sq = Square(9)
print_area(cir)
print_area(rec)
print_area(sq)