class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        KEYBOARD = {
          '2': 'abc',
          '3': 'def',
          '4': 'ghi',
          '5': 'jkl',
          '6': 'mno',
          '7': 'pqrs',
          '8': 'tuv',
          '9': 'wxyz',
        }
        def dfs(current, result):
          if len(current) == len(digits):
            result.append(''.join(current))
            return

          next_number = digits[len(current)]
          for index, char in enumerate(KEYBOARD[next_number]):
            current.append(char)
            dfs(current, result)
            current.pop()
        
        result = []
        dfs([], result)
        return result