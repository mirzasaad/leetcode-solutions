class Solution:
  def sumSubarrayMins(self, A):
    n, mod = len(A), 10**9 + 7
    left, right = [0] * n, [0] * n
    
    stack = []
    for i in range(n):
      count = 1
      while stack and stack[-1][0] > A[i]: count += stack.pop()[1]
      left[i] = count
      stack.append([A[i], count])
    
    stack = []
    for i in range(n)[::-1]:
      count = 1
      while stack and stack[-1][0] >= A[i]: count += stack.pop()[1]
      right[i] = count
      stack.append([A[i], count])
    
    return sum(a * l * r for a, l, r in zip(A, left, right)) % mod