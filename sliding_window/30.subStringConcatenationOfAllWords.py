class Solution:
  def findSubstring(self, S: str, words: List[str]) -> List[int]:
    if not words or not S: return []
    map, result = collections.Counter(words), []
    wordLength, N = len(words[0]), len(S)
    
    for skip in range(wordLength):
      counter, start, current = 0, skip, collections.Counter()

      end = skip
      while end + wordLength <= N:
        st = S[end:end + wordLength]

        if st in map:
          current[st] += 1
          if current[st] <= map[st]: counter += 1

          while map[st] < current[st]:
            temp = S[start:start + wordLength]
            current[temp] -= 1
            if map[temp] > current[temp]: counter -= 1
            start += wordLength

          if counter == len(words):
            result.append(start)
            temp = S[start:start + wordLength]
            current[temp] -= 1
            start += wordLength
            counter -= 1
        else:
          start = end + wordLength
          current.clear()
          counter = 0

        end += wordLength

        return result