"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
   """Test the calc module"""
   # Here test class should start with test unless it would not get picked up by test class
   def test_add_numbers(self):
      """Test adding numbers together."""
      res=calc.add(2,8)
      self.assertEqual(res,10)
    
   def test_subtract_numbers(self):
      """Test subracting numbers together"""
      res=calc.subtract(5,2)
      self.assertEqual(res,3)
