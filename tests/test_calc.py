import unittest

from calc import calc


class TestOperation(unittest.TestCase):

	def test_sum(self):
		self.assertEqual(calc(2, 3, 'sum'), 5, msg="Test add 2 and 3 failed to return 5")

	def test_subtract(self):
		self.assertEqual(calc(5, 10, 'subtract'), -5, msg="Test subtract 5 and 10 failed to return -5")

	def test_multiply(self):
		self.assertEqual(calc(5, 10, 'multiply'), 50, msg="Test multiply 5 and 10 failed to return 50")

	def test_divide(self):
		self.assertEqual(calc(5, 10, 'divide'), 0.5, msg="Test divide 5 and 10 failed to return 0.5")
		

if __name__ == '__main__':
	unittest.main()
		