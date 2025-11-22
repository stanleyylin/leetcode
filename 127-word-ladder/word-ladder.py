class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        L = len(beginWord)

        patterns = defaultdict(list)
        for word in wordList:
            for i in range(L):
                patterns[word[:i] + "_" + word[i + 1:]].append(word)
        
        dq = deque([beginWord])
        dist = { beginWord: 1}
        while dq:
            word = dq.popleft()

            if word == endWord:
                return dist[word]

            for i in range(L):
                pat = word[:i] + "_" + word[i+1:]
                for nei in patterns[pat]:
                    if nei not in dist:
                        dist[nei] = dist[word] + 1
                        dq.append(nei)
                    patterns[pat] = []

        return 0



            

