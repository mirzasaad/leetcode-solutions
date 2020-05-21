class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    distance, start, end, counter, map = 0, 0, 0, 0, collections.Counter()

    while end < len(s):
      ch = s[end]
      map[ch] += 1
      if map[ch] > 1: counter += 1
      end += 1

      while counter > 0:
        temp = s[start]
        if map[temp] > 1: counter -= 1
        map[temp] -= 1
        start += 1

      distance = max(distance, end - start)

    return distance