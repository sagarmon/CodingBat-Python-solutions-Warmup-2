'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
'''

def array_front9(nums):
  if len(nums) > 4:
    for i in range(4):
      if nums[i] == 9:
        return True
  elif len(nums) < 4:
    for num in nums:
      if num == 9:
        return True
  return False
