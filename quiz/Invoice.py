
def rotate(self, nums: List[int], k: int) -> None:
    # loop `k` amount of times
    for i in range(k):
        # set previous temp variable
        # .. to the last item
        prev = nums[-1]
        # loop through the array/list
        for j in range(len(nums)):
            # swap the elements
            nums[j], prev = prev, nums[j]
