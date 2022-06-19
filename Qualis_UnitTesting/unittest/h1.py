import inspect
import re
import unittest
import math
# Define class 'Circle' and its methods with proper doctests:
class Circle:
    
    def __init__(self, radius):
        # Define initialization method:
        if not isinstance(radius, (int, float)):

            raise TypeError("radius must be a number")

        if not 1000 >=radius >=0:

            raise ValueError("radius must be between 0 and 1000 inclusive")

        self.radius=radius
        
    def area(self):
        # Define area functionality:
        return math.round(math.pi*(self.radius**2),2)      
    def circumference(self):
        # Define circumference functionality:
        return  math.round(math.pi*(self.radius*2),2)

        
class TestCircleCreation(unittest.TestCase):

    def test_creating_circle_with_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5, and check if 
        # the value of c1.radius is equal to 2.5 or not.
        c1 = Circle(2.5)

        self.assertEqual(c1.radius, 2.5)

    def test_creating_circle_with_negative_radius(self):
        # Define a circle 'c' with radius -2.5, and check 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive".
        with self.assertRaises(ValueError) as e:

            c = Circle(-2.5)

        self.assertEqual(str(e.exception),"radius must be between 0 and 1000 inclusive")

    def test_creating_circle_with_greaterthan_radius(self):
        # Define a circle 'c' with radius 1000.1, and check 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive".        
        with self.assertRaises(ValueError) as e:

            c = Circle(1000.1)

        self. assertEqual(str(e.exception),"radius must be between 0 and 1000 inclusive")

    def test_creating_circle_with_nonnumeric_radius(self):
        # Define a circle 'c' with radius 'hello' and check 
        # if it raises a TypeError with the message
        # "radius must be a number".        
        with self.assertRaises (TypeError) as e:

            c = Circle('hello')

        self.assertEqual(str(e.exception),"radius must be a number")

if __name__ == '__main__':
    
    fptr = open('output.txt', 'w')
    
    runner = unittest.TextTestRunner(fptr)
    
    unittest.main(testRunner=runner, exit=False)
    
    fptr.close()
    
    with open('output.txt') as fp:
        output_lines = fp.readlines()
    
    
    pass_count = len(re.findall(r'\.', output_lines[0]))
                       
    print(str(pass_count))
                       
    doc1 = inspect.getsource(TestCircleCreation.test_creating_circle_with_numeric_radius)
    doc2 = inspect.getsource(TestCircleCreation.test_creating_circle_with_negative_radius)
    doc3 = inspect.getsource(TestCircleCreation.test_creating_circle_with_greaterthan_radius)
    doc4 = inspect.getsource(TestCircleCreation.test_creating_circle_with_nonnumeric_radius)
    
    assert1_count = len(re.findall(r'assertEqual', doc1))
    
    print(str(assert1_count))
    
    assert1_count = len(re.findall(r'assertEqual', doc2))
    assert2_count = len(re.findall(r'assertRaises', doc2))
    
    print(str(assert1_count), str(assert2_count))
    
    assert1_count = len(re.findall(r'assertEqual', doc3))
    assert2_count = len(re.findall(r'assertRaises', doc3))
    
    print(str(assert1_count), str(assert2_count))
    
    assert1_count = len(re.findall(r'assertEqual', doc4))
    assert2_count = len(re.findall(r'assertRaises', doc4))
    
    print(str(assert1_count), str(assert2_count))
    
    