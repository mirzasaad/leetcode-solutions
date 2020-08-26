class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not any(image): return image
        if image[sr][sc] == newColor: return image
        def isValid(sr, sc):
            return 0 <= sr < len(image) and 0 <= sc < len(image[0])

        def dfs(image, sr, sc, oldColor):
            if not isValid(sr, sc) or image[sr][sc] != oldColor: return

            image[sr][sc] = newColor

            dfs(image, sr-1, sc, oldColor)
            dfs(image, sr+1, sc, oldColor)
            dfs(image, sr, sc-1, oldColor)
            dfs(image, sr, sc+1, oldColor)
         

        dfs(image, sr, sc, image[sr][sc])
        return image