# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return min(left, right) + 1 if (left and right) else (left or right) + 1
    
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        q = collections.deque([root])
        depth = 0
        while q:
            depth += 1
            size = len(q)
            for _ in range(size):
                node = q.pop()
                if not node.left and not node.right:
                    return depth
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return depth