# class TwoSum(object):
#
#    """
#    For an example, suppose the array is like A = [2, 8, 12, 15],
#    and the target sum is 20. Then it will return indices 1 and 2,
#    as A[1] + A[2] = 20.
#
#    """
   
def two_Sum(number, target):
   required_index = {}
      
   for index in range(len(number)):
      if target - number[index] in required_index:
         return [required_index[target - number[index]],index]
      else:
         required_index[number[index]]= index

# user_input_list = [2,2,12,15]
# object1 = TwoSum()
# print(object1.two_Sum(user_input_list, 27))

# a, b, c, d= input("Enter four number: ").split()
# total= a, b, c, d
#
# classObject= TwoSum()
# print(classObject.two_Sum(total,total))