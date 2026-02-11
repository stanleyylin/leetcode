class Solution:
    def lengthOfLongestSubstringSW(self, s: str) -> int:
        chars = Counter()
        left = right = 0
        n = len(s)
        
        res = 0
        while left < n:
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        charToNextIndex = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in charToNextIndex:
                i = max(charToNextIndex[s[j]], i)
            
            ans = max(ans, j - i + 1)
            charToNextIndex[s[j]] = j + 1
        return ans