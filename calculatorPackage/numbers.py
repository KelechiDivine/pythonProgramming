class PositiveAndNegativeNumbers(object):
   
   def check_if_two_numbers_are_positive(self, first_number, second_number) -> bool:
      if (first_number >= 0 and second_number >= 0):
         print(f"{first_number} and {second_number} are both positive numbers.")
      
      if (first_number > 0):
         print(f"{first_number} is a positive number.")

      if (second_number > 0):
         print(f"{second_number} is a positive number.");
      
      return True
         
   def check_if_two_numbers_are_negative(self, first_number, second_number) -> bool:
      if (first_number < 0 and second_number < 0):
         print(f"{first_number} and {second_number} are both negative numbers.")

      if (first_number < 0):
         print(f"{first_number} is a negative number.");
      
      if (second_number < 0):
         print(f"{second_number} is a negative number.");
      
      return True
   
   def check_if_first_number_is_positive(self, first_number)-> bool:
      if first_number >= 0:
         print(f"{first_number} is a positive number.")

      return True
   
   def check_if_first_number_is_negative(self, first_number) -> bool:
      if first_number < 0:
         print(f"{first_number} is a negative number.")

      return True
   
   def check_if_second_number_is_positive(self, second_number)-> bool:
      if second_number >= 0:
         print(f"{second_number} is a positive number.")

      return True
   
   
   def check_if_second_number_is_negative(self, second_number)-> bool:
      if second_number < 0:
         print(f"{second_number} is a negative number.")

      return True