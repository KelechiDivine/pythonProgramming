class BincomInterview(object):
   
   def multiples_of_number(self, unknown):
      for x in unknown in range(1, 101):
         if x % 15 == 0:
            print("FizzBuzz...")
         
         elif x % 3 == 0:
            print("Buzz...")

         elif x % 5 == 0:
            print("Fizz...")
         else:
            print(x)