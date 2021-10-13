class SubCharge(object):

   def add_with_subCharge(self, first_num, second_num)-> int:
      sum = first_num + second_num
      
      if(first_num + second_num > 10):
         sum = 2
         print(f"SubCharge is {sum}")
      
      if(first_num + second_num <= 10):
         sum = 1
         print(f"SubCharge is {sum}")
         
      return sum