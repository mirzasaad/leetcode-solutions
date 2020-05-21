def generateTrees(self, n: int):
    if n == 0: return []
    return self.generateNBSTS(1, n)

def generateNBSTS(self, start, end):
list = []
if start > end: list.append(None)

for index in range(start, end+1):
    leftList = self.generateNBSTS(start, index-1)
    rightList = self.generateNBSTS(index+1, end)

    for left in leftList:
    for right in rightList:
        node = TreeNode(index)
        node.left = left
        node.right = right
        list.append(node)

return list