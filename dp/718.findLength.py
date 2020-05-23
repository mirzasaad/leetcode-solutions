class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # return self.findLength_efficient(A, B)

        m, n = len(A), len(B)
        dp = [0 for _ in range(m + 1)]
        length = 0

        for i in range(1, n + 1):
          for j in reversed(range(1, m + 1)):
            if B[i - 1] == A[j - 1]:
              dp[j] = dp[j - 1] + 1
              length = max(length, dp[j])
            else:
              dp[j] = 0

        return length
    
    def findLength_efficient(self, A, B) -> int:
      lo, hi = 1, min(len(A), len(B))
      max_length = 0

      while lo <= hi:
        mid = lo + (hi - lo) // 2
        if self.check_hash(A, B, mid):
          max_length, lo = mid, mid + 1
        else:
          hi = mid - 1
      return max_length

    def powxy(self, x, n, MOD):
      if not n: return 1
      if n < 0:
        n = -n
        x = 1/x
      result = 1
      while n > 0:
        if n & 1: result = (result * x) % MOD
        x = (x*x) % MOD
        n >>= 1
      return result

    def check_hash(self, A, B, k):
      MOD, prime, hash = 1e9 + 7, 233, 0
      m, n, result = len(A), len(B), set()
      TEMP = self.powxy(prime, k-1, MOD)
      for i in range(m):
        if i >= k:
          hash = hash + MOD - A[i-k] * TEMP % MOD
        hash = (hash * prime + A[i]) % MOD
        if i >= k - 1:
          result.add(hash)

      hash = 0
      for i in range(n):
        if i >= k:
          hash = hash + MOD - B[i-k] * TEMP % MOD
        hash = (hash * prime + B[i]) % MOD
        if i >= k - 1 and hash in result:
          return True

      return False