class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, path, sum, result):
          if sum == target:
            result.append(path[:])
            return
          if sum > target: return

          for i in range(start, len(candidates)):
            d = candidates[i]
            path.append(d)
            dfs(i, path, sum + d, result)
            path.pop()

        result = []
        dfs(0, [], 0, result)
        return result