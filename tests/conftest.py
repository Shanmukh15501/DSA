import pytest
import source.shapes  as shapes

@pytest.fixture
def my_rectange():
    return shapes.Rectangle(1,2)

@pytest.fixture
def second_rectange():
    return shapes.Rectangle(11,2)