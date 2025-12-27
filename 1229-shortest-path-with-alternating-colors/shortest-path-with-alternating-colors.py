class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_adj = [[] for _ in range(n)]
        blue_adj = [[] for _ in range(n)]

        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)
        
        # visited[node][0] -> last edge was red
        # visited[node][1] -> last edge was blue
        visited =[[False, False] for _ in range(n)]
        res = [-1] * n

        queue = deque()
        queue.append((0, 0)) # last color = red
        queue.append((0, 1)) # last color = blue
        visited[0][0] = visited[0][1] = True

        steps = 0
        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()

                if res[node] == -1:
                    res[node] = steps

                if color == 0: # last color was red -> take blue
                    for nei in blue_adj[node]:
                        if not visited[nei][1]:
                            visited[nei][1] = True
                            queue.append((nei, 1))
                else: # last was blue -> take red
                    for nei in red_adj[node]:
                        if not visited[nei][0]:
                            visited[nei][0] = True
                            queue.append((nei, 0))
            steps += 1
        return res
