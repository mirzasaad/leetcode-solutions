class Solution:
  def subarraySum(self, A, K):
    count = collections.Counter()
    count[0] = 1
    result = currentSum = 0
    for num in A:
      currentSum += num
      result += count[currentSum-k]
      count[currentSum] += 1
    return result