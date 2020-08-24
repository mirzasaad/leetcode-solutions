# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        level, result = [root], []
        while level and root:
            result.append(level[-1].val)
            level = [child for node in level for child in (node.left, node.right) if child]
        return result