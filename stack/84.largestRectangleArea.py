class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area, stack = 0, [-1]
        heights.append(0)

        for i, h in enumerate(heights):
          while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, width * height)
          stack.append(i)
        return max_area