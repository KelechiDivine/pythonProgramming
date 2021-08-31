import unittest
from Invoice import *

class InvoiceTestClass(unittest.TestCase):
    
    def test_create_price_item_is_below_0(self):
        var_invalid_price_item = Invoice()
        var_invalid_price_item.set_price_item(-8)
        self.assertEqual(0.0, var_invalid_price_item.get_price_item())
        
    def test_create_price_item_is_above_0(self):
        var_valid_price_item = Invoice()
        var_valid_price_item.set_price_item(1)
        self.assertEqual(1, var_valid_price_item.get_price_item())
        
        
    def test_check_if_invoice_amount_isvalid(self):
        var_invoice_amount = Invoice()
        var_invoice_amount.check_invoice_amout_if_its_negative(-1)
        self.assertEqual(0, var_invoice_amount.get_invoice_amount())
    
    
    def test_calculate_invoice_amount(self):
        invoice_variable = Invoice()
        invoice_variable.get_invoice_amount(4.6)
        self.assertEqual(4.6, invoice_variable.get_invoice_amount())

if __name__ == '__main__':
    unittest.main()
