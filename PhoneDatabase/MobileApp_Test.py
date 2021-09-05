import unittest
from MobileApp import PhoneBook

class MyTestCase(unittest.TestCase):

    def test_add_name_to_phoneBook(self):
        phoneBook = PhoneBook()
        phoneBook.add_name("kelechi")
        self.assertTrue("kelechi")
        
        
    def test_search_by_name(self):
        new_phoneBook = PhoneBook()
        new_phoneBook.search_method("Divine")
        self.assertTrue("Divine")

if __name__ == '__main__':
    unittest.main()
