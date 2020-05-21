class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    if not s or not p: return []
    tdict, pdict = collections.Counter(), collections.Counter()

    m, n, positions = len(s), len(p), []
    if n > m: return []
    for i in range(n):
      tdict[s[i]] += 1
      pdict[p[i]] += 1

    for i in range(n, m+1):
      if tdict == pdict:
        positions.append(i-n)

      tdict[s[i-n]] -= 1
      if i < m: tdict[s[i]] += 1
      if tdict[s[i-n]] == 0:
        del tdict[s[i-n]]

    return positions
    
    def findAnagrams2(self, text: str, pattern: str):
      result = []
      map = collections.Counter()
      
      for char in pattern:
        map[char] += 1
      
      count = len(map)
      start, end = 0, 0

      while end < len(text):
        ch = text[end]

        if ch in map:
          map[ch] -= 1
          if map[ch] == 0: count -= 1

        end += 1

        while count == 0:
          temp = text[start]

          if temp in map:  
            map[temp] += 1
            if map[temp] > 0: count += 1
          
          if end - start == len(pattern):
            result.append(start)

          start += 1
      return result  