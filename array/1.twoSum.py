class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for index, num in enumerate(nums):
            value = target - num
            if value in table:
                return [table[value], index]
            table[num] = index
        return []
