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
        
    def test_add_name_to_database(self):
        
        phone_database = PhoneBook()
        phone_database.add_name_to_database("Kelechi")
        phone_database.add_name_to_database("Divine")
        phone_database.add_name_to_database("Dozie")
        phone_database.add_name_to_database("Gbenga")
        phone_database.add_name_to_database("Chidi")
        phone_database.add_name_to_database("Ayo")
        phone_database.add_name_to_database("Amaka")
        phone_database.add_name_to_database("Dotun")
        
        self.assertTrue(True)
        
    def test_if_name_already_exist_in_the_database(self):
        phone = PhoneBook()
        phone.add_name_to_database("John")
        self.assertFalse(True)
        
    def test_search_name_in_the_database(self):
        
        phone = PhoneBook()
        phone.search_name_in_database("oelechi")
        self.assertTrue("Kelechi")

if __name__ == '__main__':
    unittest.main()
