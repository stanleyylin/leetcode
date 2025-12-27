class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        
        queue = deque([(headID, 0)])
        max_time = 0

        while queue:
            emp, time = queue.popleft()
            max_time = max(max_time, time)

            for sub in graph[emp]:
                queue.append((sub, time + informTime[emp]))
        
        return max_time
