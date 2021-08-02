import unittest
from account import test_the_file


class AccountTest(unittest.TestCase):
	 def test_account_sum(self):
		variable_sum= test_the_file(2, 3)
		self.assertEqual(5, variable_sum)