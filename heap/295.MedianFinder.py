from heapq import heappush, heappop, heappushpop
import random

class MedianFinder:

    def __init__(self):
        self.heap_max = []
        self.heap_min = []        

    def addNum(self, num: int) -> None:
        heap_max = self.heap_max
        heap_min = self.heap_min
        heappush(heap_min, -heappushpop(heap_max, num))
        if len(heap_max) < len(heap_min):
            heappush(heap_max, -heappop(heap_min))

    def findMedian(self) -> float:
        heap_max = self.heap_max
        heap_min = self.heap_min
        if len(heap_max) > len(heap_min):
            return heap_max[0]
        return (heap_max[0] - heap_min[0]) / 2.0