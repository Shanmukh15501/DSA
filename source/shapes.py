from abc import ABC,abstractmethod
import math
import time 

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius  = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

    def test_long_running(self):
        time.sleep(100)
        return 100

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length *  self.breadth
    
    def perimeter(self):
        return 2 * (self.length +  self.breadth)