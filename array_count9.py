'''
Given an array of ints, return the number of 9's in the array.
'''

def array_count9(nums):
  result = 0
  for num in nums:
    if num == 9:
      result += 1
  return result
