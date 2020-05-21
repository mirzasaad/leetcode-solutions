class Solution:
    def minWindow(self, text: str, pattern: str) -> str:
      if len(pattern) > len(text): return ''
      Index = collections.namedtuple('Index', 'start length')

      start, end, dict = 0, 0, collections.Counter(pattern)
      substr = Index(0, 1<<31)    
      count = len(dict)

      while end < len(text):
        char = text[end]
        if char in dict:
          dict[char] -= 1
          if dict[char] == 0: count -= 1

        end += 1

        while count == 0:
          temp = text[start]
          if temp in dict:
            dict[temp] += 1
            if dict[temp] > 0: count += 1

          if substr.length > end - start:
            substr = Index(start, end - start)
          start += 1
      if substr.length == 1<<31: return ''
      return text[substr.start:substr.start+substr.length]