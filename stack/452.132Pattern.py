class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, Interval = [], collections.namedtuple('Interval', 'min max')
    
        for x in nums:
          if not stack or (stack and x < stack[-1].min):
            stack.append(Interval(x, x))
          elif x > stack[-1].min:
            last = stack.pop()
            if x < last.max: return True
            elif x >= last.max:
              last = Interval(last.min, x)
              while stack and last.min <= stack[-1].min and last.max >= stack[-1].max:
              # while stack and x >= stack[-1].max:
                stack.pop()

              if stack and x < stack[-1].max and x > stack[-1].min: return True
              stack.append(last)

        return False