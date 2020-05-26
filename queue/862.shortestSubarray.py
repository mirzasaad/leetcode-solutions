class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
      current, deque, length = 0, collections.deque([(0,0)]), len(A) + 1
      
      for end in range(len(A)):
        current += A[end]

        while deque and current - deque[0][1] >= K:
          length = min(length, end + 1 - deque.popleft()[0])

        while deque and current <= deque[-1][1]:
          deque.pop()

        deque.append((end + 1, current))

      return -1 if length == len(A) + 1 else length