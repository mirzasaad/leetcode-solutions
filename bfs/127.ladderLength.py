class Solution:
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def getNextWords(word):
            for i in range(len(beginWord)):
                for character in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + character + word[i + 1:]
                    yield next_word
        
        wordList = set(wordList)
        q = collections.deque([beginWord])
        level = 0
        while q:
            level += 1
            size = len(q)
            for _ in range(size):
                word = q.popleft()
                if word == endWord: return level
                for next_word in getNextWords(word):
                    if next_word in wordList:
                        wordList.remove(next_word)
                        q.append(next_word)
        return 0
    
    def ladderLengthImproved(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or endWord not in wordList: return 0
        adjacent = collections.defaultdict(list) 

        for word in wordList:
        for i in range(len(word)):
            adjacent[word[:i] + '*' + word[i+1:]].append(word)

        q = collections.deque([(beginWord, 1)])
        visited = collections.defaultdict(bool)
        visited[beginWord] = True

        while q:
        word, depth = q.popleft()
        for i in range(len(word)):
            next_word = word[:i] + '*' + word[i+1:]
            for w in adjacent[next_word]:
            if w not in visited:
                if w == endWord: return depth + 1
                visited[w] = True
                q.append((w, depth + 1))
        
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord: return 0
        adjacent = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                adjacent[word[:i] + "*" + word[i+1:]].append(word)

        def visit(q, visited, visited_other):
            word, depth = q.popleft()
            for i in range(len(word)):
                next_word = word[:i] + '*' + word[i+1:]
                for w in adjacent[next_word]:
                    if w in visited_other:
                        return visited_other[w] + depth
                    if w not in visited:
                        visited[w] = depth + 1
                        q.append((w, depth + 1))
            return None

        visited_start, visited_end = {beginWord:1}, {endWord:1}
        q1, q2 = collections.deque([(beginWord, 1)]), collections.deque([(endWord, 1)])

        while q1 and q2:
            result = visit(q1, visited_start, visited_end) or \
                        visit(q2, visited_end, visited_start)
            if result: return result
        return 0 