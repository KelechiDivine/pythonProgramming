class ArrayValue(object):

   def to_array(self, first_arg:int, second_arg:int) -> list:
      integer_array_list: list = []
      integer_array_list.insert(0, first_arg)
      integer_array_list.insert(1, second_arg)
      print(f"Successfully converted {first_arg} and {second_arg} to an array.")
      return integer_array_list