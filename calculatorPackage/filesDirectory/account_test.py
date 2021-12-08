import unittest
from account import test_the_file


class AccountTest(unittest.TestCase):
    def test_account_sum(self) -> int:
        variable = test_the_file(1, 4)
        self.assertEqual(5, variable)
        print(variable)
        self.countTestCases()
        print(self.countTestCases())
