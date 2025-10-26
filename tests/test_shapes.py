import source.shapes as shapes
import math

class TestCircle:
    
    def setup_method(self,method):
        print(f'Invoking the method {method}')
        self.circle  = shapes.Circle(10)
    
    def teardown_method(self,method):
        print(f'Test completed for  {method}')
        del self.circle
    
    def test_area(self):
        assert self.circle.area() == math.pi*((self.circle.radius)**2)
    
    def test_permiter(self):
        assert self.circle.perimeter() == 2* math.pi*self.circle.radius
        
    def test_validate_areas(self,second_rectange):
        assert second_rectange.area() !=  self.circle.area()
    

        
        