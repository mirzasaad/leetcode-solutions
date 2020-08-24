# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        level, result, direction = [root], [], 1
        while level and root:
            result.append([node.val for node in level][::direction])
            level = [child for node in level for child in (node.left, node.right) if child]
            direction *= -1
        return result