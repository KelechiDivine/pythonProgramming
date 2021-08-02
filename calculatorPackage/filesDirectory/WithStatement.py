with open("account.py", mode= 'w') as accounts:
    # accounts.write("100 Jones 24.98\n")
    # accounts.write("200 Doe 345.67\n")
    # accounts.write("300 Smith 0.00\n")
    # accounts.write("400 Kelechi 534.78\n")
    # accounts.write("500 Rich 224.62\n")
    # accounts.write("600 Stone -24.98\n")
    # accounts.write("700 Okoroafor 24.98\n")
    accounts.write("def test_the_file(firstnum, secondnum):\n\t"
                   "sum= firstnum + secondnum\n\t"
                   "return sum")
    
    
with open("account_test.py", mode= 'w') as accountTest:
    accountTest.write("import unittest\n"
                      "from account import test_the_file\n\n\n"
                      "class AccountTest(unittest.TestCase):\n\t "
                      "def test_account_sum(self):\n\t\t "
                      "variable_sum= test_the_file(2, 3)\n\t\t\t\t"
                      "     self.assertEqual(5, variable_sum)")
print(accounts)