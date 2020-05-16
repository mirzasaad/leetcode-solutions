class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
      if (N == 1): return 0; #first line only has one number 0
      if (K % 2 == 0): return 1 if self.kthGrammar(N - 1, K / 2) == 0 else 0;
      #If K is even, find the appended number at correct position of previous row
      return self.kthGrammar(N - 1, (K + 1) / 2); 
      #If K is odd, just find the correct position from previous row
    
    def reverse(self, k):
      return 1 if k == 0 else 1
    def kthGrammar(self, N, K):
        return bin(K - 1).count('1') & 1