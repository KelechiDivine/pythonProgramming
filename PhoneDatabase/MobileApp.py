import re

class PhoneBook(object):
   #
   # def __init__(self, search, service_number, add_name, erase, edit,
   #              assign_tones, send_b_card, options, speed_dial, voice_tag):
   #
   #     self.search = search
   #     self.service_number = service_number
   #     self.add_name = add_name
   #     self.erase = erase
   #     self.edit = edit
   #     self.assign_tone = assign_tones
   #     self.send_b_card = send_b_card
   #     self.options = options
   #     self.speed_dial = speed_dial
   #     self.voice_tag = voice_tag
   #
   #
   
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
   
   # def display_phone_book_menu(self, menu) -> str:
   #     if menu == "Phone Book Menu":
   #         return
   #