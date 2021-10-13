class Script(object):
   
   def return_true_if_sum_of_two_numbers_is_50(self, firstNumber, secondNumber)-> bool:
      if firstNumber + secondNumber == 50:
         print(f"The sum of {firstNumber} and {secondNumber} is 50.")
         
      if firstNumber + secondNumber != 50:
         print(f"The sum of {firstNumber} and {secondNumber} is not 50.")
      
      return True
   
   def return_true_if_first_number_is_50(self, firstNumber)-> bool:
      if firstNumber == 50:
         print(f"The first number is {firstNumber}.")
      
      if firstNumber != 50:
         print("The first number is not 50.")
         
      return True
   
   def return_true_if_second_number_is_50(self, secondNumber)-> bool:
      if secondNumber == 50:
         print(f"The second number is {secondNumber}.")
         
      if secondNumber != 50:
         print("The second number is not 50.")
         
      return True
   
   
   