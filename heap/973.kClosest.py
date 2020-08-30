import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap, result = [], []
        for pt in points:
            heapq.heappush(heap, ( sqrt(pt[0] ** 2 + pt[1] ** 2) , pt ))
        
        for _ in range(K):
            _, pt = heapq.heappop(heap)
            result.append(pt)
        
        return result