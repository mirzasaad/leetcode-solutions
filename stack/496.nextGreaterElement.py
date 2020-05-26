class Solution:
    def nextGreaterElement(self, findNums: List[int], nums: List[int]) -> List[int]:
        map, stack, result = {}, [], [-1] * len(findNums)
        for x in nums:
          while stack and stack[-1] < x:
            map[stack.pop()] = x
          stack.append(x)

        for i, x in enumerate(findNums):
          result[i] = map.get(x, -1)

        return result