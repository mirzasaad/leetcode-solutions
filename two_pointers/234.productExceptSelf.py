import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:   
        temp, prod, N = 1, [1] * len(nums), len(nums)
        for i in range(N):
            prod[i] *= temp
            temp *= nums[i]
        temp = 1
        for i in reversed(range(N)):
            prod[i] *= temp
            temp *= nums[i]
        return prod
  # log10 solution, non zero based, as there is no log10(0)
  def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        total_sum = sum(math.log10(num) for num in nums)
        return [int(1e-9 + math.pow(10.00, total_sum - math.log10(num))) for num in nums]
        