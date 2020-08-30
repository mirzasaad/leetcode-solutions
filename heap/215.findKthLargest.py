import heapq
from typing import List
from random import randint

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
    
    def partition(self, A, left, right):
        pivot = A[right]
        next_index = left
        
        for i in range(left, right):
            if A[i] < pivot:
                A[i], A[next_index] = A[next_index], A[i]
                next_index += 1
                
        A[next_index], A[right] = A[right], A[next_index]
        return next_index
    
    def partition_random(self, A, left, right):
        ri = randint(left, right)
        pivot = A[ri]
        next_index = left

        A[ri], A[right] = A[right], A[ri]

        for i in range(left, right + 1):
            if A[i] > pivot:
                A[i], A[next_index] = A[next_index], A[i]
                next_index += 1
        A[next_index], A[right] = A[right], A[next_index]
        return next_index

    def findKthLargestQuickSelect(self, nums, k):
        left, right, k = 0, len(nums) - 1, k
        
        while left <= right:
            pi = self.partition_random(nums, left, right)

            if pi == k - 1:
                return nums[pi]
            elif pi < k - 1:
                left = pi + 1
            else:
                right = pi - 1
        
        return None