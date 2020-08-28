class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area, N = 0, len(heights)
        lessfromleft, lessfromright = [-1 for _ in range(N)], [N for _ in range(N)]
        
        for i in range(1, N):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = lessfromleft[p]
            lessfromleft[i] = p
        
        for i in reversed(range(N - 1)):
            p = i + 1
            while p < N and heights[p] >= heights[i]:
                p = lessfromright[p]
            lessfromright[i] = p
        
        for i in range(N):
            width = lessfromright[i] - lessfromleft[i] - 1
            height = heights[i]
            max_area = max(max_area, width * height)
        
        return max_area