
import pytest 
import  source.shapes as shapes

def test_area_of_rectangle(my_rectange):
    assert my_rectange.area() == 1*2

def test_permiter_of_rectangle(my_rectange):
    assert my_rectange.perimeter() == 2*(1+2)

def test_two_rectangles(my_rectange,second_rectange):
    print("Comparing areas of two rectange objects")
    assert my_rectange.area() != second_rectange.area()
    
    
@pytest.mark.just
@pytest.mark.parametrize("l,b,eans",[(2,1,6),(3,1,8),(70,80,300)])
def test_single_param_rectangle(l,b,eans):
    assert shapes.Rectangle(l,b).perimeter() == eans

