class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxRank = 0

        adj = defaultdict(set)

        for city1, city2 in roads:
            adj[city1].add(city2)
            adj[city2].add(city1)

        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                currentRank = len(adj[node1]) + len(adj[node2])
                if node2 in adj[node1]:
                    currentRank -= 1
                maxRank = max(maxRank, currentRank)
        return maxRank

        