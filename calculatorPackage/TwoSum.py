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
