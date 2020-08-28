class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        maxFromLeft, maxFromRight = [0] * N, [0] * N

        max_left_wall = 0
        for i in range(N):
            maxFromLeft[i] = max_left_wall
            max_left_wall = max(max_left_wall, height[i])

        max_right_wall = 0
        for i in reversed(range(N)):
            maxFromRight[i] = max_right_wall
            max_right_wall = max(max_right_wall, height[i])

        total = 0
        for i, elevation in enumerate(height):
            lowest_wall = min(maxFromLeft[i], maxFromRight[i])
            if lowest_wall > elevation:
                total += lowest_wall - elevation
        return total