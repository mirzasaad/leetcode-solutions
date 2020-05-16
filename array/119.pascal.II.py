class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        line = [1]
        n = rowIndex
        for k in range(n):
          line.append(line[k] * (n-k)//(k+1))
        return line