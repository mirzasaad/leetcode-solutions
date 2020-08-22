class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        lo, hi = 0, N - 1

        while lo < hi:
          mid = lo + ((hi-lo)//2)
          if nums[mid] > nums[hi]: lo = mid + 1
          else: hi = mid

        rotation, lo, hi = lo, 0, N-1
        while lo <= hi:
          mid = lo + ((hi-lo)//2)
          realmid = (mid+rotation) % N
          if nums[realmid] == target: return realmid
          if target > nums[realmid]: lo = mid + 1
          else: hi = mid - 1
        return -1