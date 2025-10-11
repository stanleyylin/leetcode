class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        vec = [(-(10**9), 0)]
        for spell in sorted(count.keys()):
            vec.append((spell, count[spell]))
        n = len(vec)
        dp = [0] * n
        maxDamage = 0
        j = 1
        for i in range(1, n):
            while j < i and vec[j][0] < vec[i][0] - 2:
                maxDamage = max(maxDamage, dp[j])
                j += 1
            dp[i] = maxDamage + vec[i][0] * vec[i][1]
        return max(dp)


