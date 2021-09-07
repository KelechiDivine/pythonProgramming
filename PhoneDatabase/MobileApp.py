import re
import numpy as np

class PhoneBook(object):
   
   def search(self):
       print("1: Search")
       
   def service_number(self):
       print("2: Service Number")
    
   def add_name(self):
        print("3: Add name")
    
   def erase(self):
       print("4: Erase")
   
   def edit(self):
       print("5: Edit")

   def assign_tone(self):
       print("6: Assign tone")
       
   
   def send_b_card(self):
       print("7: Send b's card")
       
   
   def option(self, is_navigate):
       print("8: Options")

       def navigate_options():
           if is_navigate == 8:
               print("\t-> Type Of view")
               print("\t-> Memory status")

       print(navigate_options())
       
   def speed_dials(self):
       print("9: Speed Dials")
       
   def voice_tags(self):
       print("10: Voice Tags")
       
       
       
       
       
   def add_name_to_phoneBook(self, name)->str:
       
       name_database = np.save
       name_list = [name]
       name_database = name_list
       
       if name in name_database:
           print("Name already exist.")
       
       else:
           name_database = name_list.add(name)
           print(name + " have been added to the database...")
       
       print(name_list)
       return name_database
       
       
       
       
       
       
       
       
       
   def search_name_in_database(self, search_name):
       if self.var_search(search_name):
           print(search_name + " was found in the database.")
           return self.var_search(search_name)