class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, sum, path, result):
          if sum == target:
            result.append(path[:])
            return
          if sum > target: return

          for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]: continue
            d = candidates[i]
            path.append(d)
            dfs(i + 1, sum + d, path, result)
            path.pop()

        candidates.sort(reverse=True)
        result = []
        dfs(0, 0, [], result)
        return result