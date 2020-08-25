# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        adjacent = collections.defaultdict(list)
        def connect(child, parent):
            if not child: return

            if child and parent:
                adjacent[child.val].append(parent)
                adjacent[parent.val].append(child)

            if child.left: connect(child.left, child)
            if child.right: connect(child.right, child)

        connect(root, None)

        q = collections.deque([target])
        marked = collections.defaultdict(bool)
        marked[target] = True

        for _ in range(K):
            size = len(q)
            for _ in range(size):
                v = q.popleft()
                for w in adjacent[v.val]:
                    if not marked[w]:
                        marked[w] = True
                        q.append(w)

        return [node.val for node in q]