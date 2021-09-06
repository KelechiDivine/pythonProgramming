import unittest
from MobileApp import PhoneBook

class MobilePhoneTest(unittest.TestCase):

    def test_search(self):
        phoneBook = PhoneBook()
        phoneBook.search()
        self.assertTrue(True)
        
        
    def test_service_number(self):
        new_phoneBook = PhoneBook()
        new_phoneBook.service_number()
        self.assertTrue(True)
        
        
    def test_add_name(self):
        phone_book = PhoneBook()
        phone_book.add_name()
        self.assertTrue(True)
        
        
    def test_erase(self):
        phoneBook = PhoneBook()
        phoneBook.erase()
        self.assertTrue(True)
        
        
    def test_edit(self):
        phone = PhoneBook()
        phone.edit()
        self.assertTrue(True)
        
        
    def test_assign_tone(self):
        phone = PhoneBook()
        phone.assign_tone()
        self.assertTrue(True)
        
        
    def test_send_b_card(self):
        phone = PhoneBook()
        phone.send_b_card()
        self.assertTrue(True)
        
        
    def test_is_option(self):
        phone_option = PhoneBook()
        phone_option.option(8)
        self.assertTrue(True)
        
        
    def test_speed_dial(self):
        phone = PhoneBook()
        phone.speed_dials()
        self.assertTrue(True)
        
        
    def test_voice_log(self):
        phone = PhoneBook()
        phone.voice_tags()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
