class Solution:
    def nextGreaterElement(self, n: int) -> int:
        A, N = list(str(n)), math.floor(math.log10(n)) + 1
        inversion = N - 2

        while inversion >= 0 and A[inversion] >= A[inversion + 1]:
          inversion -= 1

        if inversion == -1: return inversion

        smallest = inversion + 1
        for i in range(inversion + 1, N):
          if A[i] <= A[smallest] and A[i] > A[inversion]:
            smallest = i

        A[smallest], A[inversion] = A[inversion], A[smallest]
        A[inversion+1:N] = A[inversion+1:N][::-1]

        n = int(''.join(A))
        return n if n < 1<<31 - 1 else -1