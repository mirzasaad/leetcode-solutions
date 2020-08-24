from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level, result = [root], []
        while level and root:
            result.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
          
        return result