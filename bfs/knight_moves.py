import collections
def get_knight_shortest_path(x: int, y: int) -> int:
    Node = collections.namedtuple('Node', 'x y')
    def get_adjacent(node):
        adjacent = collections.defaultdict(list)
        delta_row = [-2, -2, -1, 1, 2, 2, 1, -1]
        delta_col = [-1, 1, 2, 2, 1, -1, -2, -2]
        for i in range(len(delta_col)):
            r = node.x + delta_row[i]
            c = node.y + delta_col[i]
            adjacent.append(Node(r, c))
        return adjacent

    q = collections.deque([Node(x, y)])
    visited = collections.defaultdict(bool)
    level = 0
    while q:
        size = len(q)
        level += 1
        for _ in range(size):
            node = q.popleft()
            if node.x == x and node.y == y: return level
            for w in get_adjacent(node):
                if not visted[node]:
                    visted[node] = True
                    q.append(node)
    return level

            