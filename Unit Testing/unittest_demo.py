"""
Unittest is another Python's built-in testing module.

Unittest is Python's xUnit-style unit testing framework.

It's functionality is similar to XUnit-style libraries in other programming languages such as JUnit in Java, CPPUnit in C++, PHPUnit in PHP, etc.

All the xUnit-style testing frameworks are derived from Smalltalk's unit testing framework SUnit.

py -m pytest unittest_demo.py -v --junitxml=result.xml

"""
#importing the unittest module
import unittest
#importing the sample module
from sample_module import add2num,pow2num

def setUpModule():
    print('Executed before an test in the module')

def tearDownModule():
    print('Executed after all tests in module are run')
#Define a class that extends the TestCase class:
class TestAdd2Num(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Executed before any test in the class runs.')

    @classmethod
    def tearDownClass(cls):
        print('Executed after all tests in class are run.')

    def setUp(self):
        print('Executed before start of every test')

    def tearDown(self):
        print('Executed at the end of every test')

    def test_add2num_with_positive_num(self):
        self.assertEqual(add2num(2,4),6)
    
    def test_add_2_num_with_negative_num(self):
        self.assertEqual(add2num(-2,1),-1)

class Testpow2num(unittest.TestCase):
    def test_pow_2pos_num(self):
        self.assertEqual(pow2num(3, 4), 81)

    def test_neg_pow(self):
        self.assertEqual(pow2num(10, -2), 0.01)

    def test_negnum_pow(self):
        self.assertEqual(pow2num(-3, 3), -26)

if __name__ == "__main__":
    unittest.main()
