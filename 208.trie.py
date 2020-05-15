import collections
class TrieNode:
  # Initialize your data structure here.
  def __init__(self):
    self.children = collections.defaultdict(TrieNode)
    self.is_word = False

  def __repr__(self):
    return '(%s =>> %s)' % (self.is_word, self.children.keys())

class Trie():
  def __init__(self):
    self.root = TrieNode()

  def insert(self, string):
    self.__insert(self.root, string, 0)
  
  def __insert(self, node, string, d):
    if d == len(string):
      node.is_word = True
      return node

    ch = string[d]
    node.children[ch] = self.__insert(node.children[ch], string, d+1)
    return node

  def search(self, string):
    return self.__search(self.root, string, 0)

  def __search(self, node, string, d):
    if not node: return False
    if d == len(string) and node.is_word: return True
    if d == len(string): return False
  
    ch = string[d]
    return self.__search(node.children[ch], string, d+1)

  def prefix(self, string):
    return self.__prefix(self.root, string, 0)

  def __prefix(self, node, string, d):
    if not node: return False
    if d == len(string): return True
    
    ch = string[d]
    return self.__prefix(node.children[ch], string, d+1)


trie = Trie()
trie.insert('abc')

print(trie.root.children['a'].children['b'].children['c'])