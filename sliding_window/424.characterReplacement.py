class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, start, length = collections.Counter(), 0, 0

        for end, st in enumerate(s):
          count[st] += 1
          common = count.most_common(1)[0][1]
          while end - common - start + 1 > k:
            count[s[start]] -= 1
            start += 1
          length = max(length, end - start + 1)

        return length