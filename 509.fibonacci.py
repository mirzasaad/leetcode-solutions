class Solution:
    def fib(self, N: int, memo = {}) -> int:
        if N <= 1: return N
        if N in memo: return memo[N]
        
        memo[N] = self.fib(N-1) + self.fib(N-2)
        return memo[N]