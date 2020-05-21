class Solution:
  def kthSmallestBSTMorrison(self, root, k):
    if k == 0: return None
    current = root

    while current:
      if not current.left:
        k -= 1
        if k == 0: return current.val
        current = current.right
      else:
        pre = current.left
        while pre.right and pre.right is not current:
          pre = pre.right

        if not pre.right:
          pre.right = current
          current = current.left
        else:
          k -= 1
          if k == 0: return current.val
          pre.right = None
          current = current.right
    return None

  def kthSmallestBST(self, root, k):
    if k == 0: return None
    stack = []
    while root or stack:
      while root:
        stack.append(root)
        root = root.left

      root = root.pop()
      k -= 1
      if k == 0: return root.val
      root = root.right