import re

class PhoneBook(object):
    
    
    def add_name(self, add_friends_name)->str :
        names_in_phone_book = []
        names_in_phone_book.append(add_friends_name)
        print(names_in_phone_book)
        return names_in_phone_book
    
    
    search_name_in_phone_book = add_name("")
    def search_method(self, search_name)->str:
        phone_book = PhoneBook()
        if search_name in re.search(phone_book.search_name_in_phone_book, search_name, []):
            print("we found a name!")
        else:
            print("no name was found.")