# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def fn(root, st, result):
          if not root: return
          if not root.left and not root.right:
            result.append(st + str(root.val))
            return
          
          fn(root.left, st + str(root.val) + "->", result)
          fn(root.right, st + str(root.val) + "->", result)
        
        result = []
        fn(root, "", result)
        return result