def monotonic_previous_less(A):
  stack, less = [], [-1] * len(A)
  for i, x in enumerate(A):
    while stack and stack[-1][1] > x:
      stack.pop()
    less[i] = stack[-1][1] if stack else -1
    stack.append((i, x))
  return less

def monotonic_next_less(A):
  stack, less = [], [-1] * len(A)
  for i, x in enumerate(A):
    while stack and stack[-1][1] > x:
      index, value = stack.pop()
      less[index] = x
    
    stack.append((i, x))
  return less

def sumSubarrayMins(A):
  n, mod = len(A), 10**9 + 7
  left, right, s1, s2 = [0] * n, [0] * n, [], []
  for i in range(n):
      count = 1
      while s1 and s1[-1][0] > A[i]: count += s1.pop()[1]
      left[i] = count
      s1.append([A[i], count])
  for i in range(n)[::-1]:
      count = 1
      while s2 and s2[-1][0] >= A[i]: count += s2.pop()[1]
      right[i] = count
      s2.append([A[i], count])

  return sum(a * l * r for a, l, r in zip(A, left, right)) % mod

print(sumSubarrayMins([2, 9, 7, 8, 3, 4, 6, 1]))