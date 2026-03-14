class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return "" # check 2nd word isn't prefix of 1st
# A shorter word must come before its prefix extension.
        
        # run kahn's algo: pick off nodes w/ indegree of 0
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)
        
        # if not all letteres in output, that means
        # there's a cycle so no valid ordering
        if len(output) < len(in_degree):
            return ""

        # otherwise output a string
        return "".join(output)

