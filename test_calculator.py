import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1,-2),-3)
    def test_add_zero(self):
        self.assertEqual(self.calc.add(1,0),1)
    def test_subtract_plus(self):
        self.assertEqual(self.calc.subtract(0,1),-1)
    def test_subtract_minus(self):
        self.assertEqual(self.calc.subtract(-4,-5),1)
    def test_multiply_plus(self):
        self.assertEqual(self.calc.multiply(4,5),20)
    def test_multiply_minus(self):
        self.assertEqual(self.calc.multiply(-4,5),-20)    
    def test_divide_plus(self):
        self.assertEqual(self.calc.divide(10,2),5)    
    def test_divide_downr(self):
        self.assertEqual(self.calc.divide(5,10),0)    
    def test_modulo_normal(self):
        self.assertEqual(self.calc.modulo(5,2),1)    
    def test_modulo_minus(self):
     self.assertEqual(self.calc.modulo(-10,0),"b cannot =0")    

if __name__ == '__main__':
    unittest.main()