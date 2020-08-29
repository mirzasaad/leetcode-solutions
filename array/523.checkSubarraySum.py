class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))
        
        prefix_mod_k, sum_mode_k = collections.defaultdict(int), 0
        prefix_mod_k[0] = -1
        for i in range(len(nums)):
            sum_mode_k = (sum_mode_k + nums[i]) % k
            if sum_mode_k in prefix_mod_k and i - prefix_mod_k[sum_mode_k] > 1:
                return True
            if not sum_mode_k in prefix_mod_k:
                prefix_mod_k[sum_mode_k] = i
        return False