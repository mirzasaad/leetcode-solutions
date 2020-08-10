import collections
class Solution:
  def minSubArrayLen(self, sum: int, nums: List[int]) -> int:
    start, end, counter, length = 0, 0, False, len(nums) + 1

    while end < len(nums):
      sum -= nums[end]
      if sum <= 0: counter = True
      end += 1

      while counter:
        sum += nums[start]
        if sum > 0: counter = False
        length = min(length, end - start)
        start += 1
    return 0 if length == len(nums) + 1 else length
