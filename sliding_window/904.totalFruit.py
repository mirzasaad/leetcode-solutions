class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        start, count = 0, collections.Counter()
        length = 0

        for end, v in enumerate(tree):
          count[v] = count.get(v, 0) + 1
          if len(count) > 2:
            count[tree[start]] -= 1
            if count[tree[start]] == 0: del count[tree[start]]
            start += 1

        return end - start + 1