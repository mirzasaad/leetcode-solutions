def findKthLargest(self, nums: List[int], k: int) -> int:
    def partition(A, lo, hi):
        pivot = A[hi]
        left = lo
        for i in range(lo, hi):
        if A[i] < pivot:
            A[left], A[i] = A[i], A[left]
            left += 1
        A[left], A[hi] = A[hi], A[left]
        return left

    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        index = partition(nums, lo, hi)
        if index == len(nums) - k:
        return nums[index]
        elif index < len(nums) - k:
        lo = index + 1
        else:
        hi = index - 1
    return -1

#random pivot
def findKthLargest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def partition(l, r):
        ri = randint(l, r)
        nums[r], nums[ri] = nums[ri], nums[r]
        for i, v in enumerate(nums[l: r+1], l):
            if v >= nums[r]:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        return l - 1
    
    l, r, k = 0, len(nums) - 1, k - 1
    while True:
        pos = partition(l, r)
        if pos < k:
            l = pos + 1
        elif pos > k:
            r = pos - 1
        else:
            return nums[pos]