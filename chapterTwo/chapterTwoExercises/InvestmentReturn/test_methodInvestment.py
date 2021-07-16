import unittest
from InvestmentReturn import invest_after_ten_years as tenYears
from InvestmentReturn import invest_after_twenty_years as twentyYears
from InvestmentReturn import investment_after_thirty_years as thirtyYears

class TestClassForInvestment(unittest.TestCase):
    def testing_ten_years_investment(self):
        ten = tenYears(1000)
        self.assertEqual(ten, 700.0)
    
    def testing_twenty_years_investment(self):
        twenty = twentyYears(1000)
        self.assertEqual(twenty, 1400)
    
    def testing_thirty_years_investment(self):
        thirty = thirtyYears(1000)
        self.assertEqual(thirty, 2100.0)
if __name__ == '__main__':
    unittest.main()
