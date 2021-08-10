import unittest
from account import test_the_file


# class AccountTest(unittest.TestCase):
# 	 def test_account_sum(self):
# 		variable_sum= test_the_file(5, 7)
# 		self.assertEqual(5, variable_sum)

class AccountTest(unittest.TestCase):
	def test_account_sum(self) -> int:
		vari= test_the_file(1, 4)
		self.assertEqual(5, vari)
		# self.assertRaisesRegex(5, expected_exception=numpy)
		print(vari)
		self.countTestCases()
		print(self.countTestCases())
