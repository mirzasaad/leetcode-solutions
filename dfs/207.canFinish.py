from typing import List
from collections import defaultdict, deque
from enum import Enum

class State(Enum):
    TO_VISIT = 0
    VISITING = 1
    VISITED = 2

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def build_graph():
            graph = defaultdict(list)
            for src, dest in prerequisites:
                graph[src].append(dest)
            return graph

        def dfs(v):
            if marked[v] == State.VISITING: return False
            if marked[v] == State.VISITED: return True
            
            marked[v] = State.VISITING

            for w in graph[v]:
                if not dfs(w): return False

            marked[v] = State.VISITED
            return True

        graph = build_graph()
        marked = defaultdict(bool)
        cyclic = [False]
        print(graph)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

solution = Solution()
print(solution.canFinish(2, [[1, 0], [0, 1]]))