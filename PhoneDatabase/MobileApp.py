import re

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
   