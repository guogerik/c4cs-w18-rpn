import unittest
import rpn

class TestBasics(unittest.TestCase):
	
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_adds(self):
		result = rpn.calculate("1 1 + 2 +")
		self.assertEqual(4, result)
	def test_subtract(self):
		result = rpn.calculate("5 2 -")
		self.assertEqual(3, result)
	def test_toomany(self):
		with self.assertRaises(TypeError):
			result = rpn.calculate("1 2 3 +")
	def test_multiply(self):
		result = rpn.calculate("4 9 *")
		self.assertEqual(36,result)
	def test_multiplys(self):
		result = rpn.calculate("2 3 * 4 *")
		self.assertEqual(24,result)
	def test_divide(self):
		result = rpn.calculate("8 4 /")
		self.assertEqual(2,result)
	def test_divides(self):
		result = rpn.calculate("20 4 / 5 /")
		self.assertEqual(1,result)
	def test_floatingdivision(self):
		result = rpn.calculate("20 4 / 2 /")
		self.assertEqual(2.5,result)
	def test_exponent(self):
		result = rpn.calculate("2 3 ^")
		self.assertEqual(8,result)
	def test_exponentneg(self):
		result = rpn.calculate("2 -1 ^")
		self.assertEqual(0.5,result)
