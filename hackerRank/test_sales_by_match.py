import unittest
from SalesByMatch import *


class MyTestCase(unittest.TestCase):

    def test_sales_by_match_class_exist(self):
        match = SalesByMatch()
        self.assertIsNotNone(match)  # add assertion here

    def test_can_count_sock_and_pair_sock_by_color(self):
        sales_by_match = SalesByMatch()
        new_match = [1, 2, 1, 2, 1, 3, 2]
        sock_variable = sales_by_match.sock_merchant(7, new_match)
        self.assertEquals(2, sock_variable, "No socks was paired.")


if __name__ == '__main__':
    unittest.main()
