# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
  def __init__(self):
    self.spliter = ","
    self.NULL = "x"
  def serialize(self, root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    def fn(node, result):
      if not node: result.append(self.NULL)
      else:
        result.append(str(node.val))
        fn(node.left, result)
        fn(node.right, result)


    result = []
    fn(root, result)
    return self.spliter.join(result)

  def deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    def fn(preorder):
      if not preorder: return
      value = preorder.popleft()
      if value == self.NULL: return None
      node = TreeNode(int(value))
      node.left = fn(preorder)
      node.right = fn(preorder)
      return node
    
    preorder = deque(data.split(','))
    root = fn(preorder)
    return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))