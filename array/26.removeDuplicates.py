class Solution:
    def removeDuplicates2(self, nums: List[int]) -> int:
        N, left, runner = len(nums), 0, 0
        if N in (0, 1):
            return N
        while runner < N - 1:
            while runner < N - 1 and nums[runner] == nums[runner + 1]:
                runner += 1
            nums[left] = nums[runner]
            left, runner = left + 1, runner + 1

        if N > 1 and nums[N - 1] != nums[N - 2]:
            nums[left] = nums[N - 1]
            left += 1
        return left
    
    def removeDuplicates(self, nums: List[int]) -> int:
        N, left = len(nums), 0
        if not nums:
            return 0
        for runner in range(N):
            if nums[left] != nums[runner]:
                left += 1
            nums[left] = nums[runner]
        return left + 1