class Solution:
    def wordBreakSolution1(self, s: str, wordDict: List[str]) -> bool:
        def dfs(index, _set):
            if index == len(s): return True
            if index in _set: return False

            for i in range(index + 1, len(s) + 1):
                substring = s[index:i]
                if substring in wordDict:
                    if dfs(i, _set): return True
                    else: _set.add(i)

            _set.add(index)
            return False
        
        return dfs(0, set())

    def wordBreakSolution2(self, s: str, wordDict: List[str]) -> bool:
        def dfs(index, memo):
            if index == len(s): return True
            if index in memo: return memo[index]

            ok = False
            for word in wordDict:
                if s[index:].startswith(word):
                    if dfs(index + len(word), memo):
                        ok = True
                        break

            memo[index] = ok
            return ok
        memo = {}
        return dfs(0, memo)
    
    def wordBreakSolutionDP(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)

        dp[0] = True

        for i in range(1, N + 1):
            for j in range(0, i):
                substring = s[j:i]
                if dp[j] and substring in wordDict:
                    dp[i] = True
                    break
        
        return dp[N]