class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i, keys in enumerate(rooms):
            graph[i] = keys
        
        visited = [False] * len(rooms)
        queue = deque([0])

        while queue:
            room = queue.popleft()
            if not visited[room]:
                visited[room] = True
                for key in graph[room]:
                    queue.append(key)
        
        return all(visited)

