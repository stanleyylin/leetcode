class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True
        
        for length in range(len(s), 0, -1):
            for i in range(len(s)-length+1):
                if check(i, i+length):
                    return s[i:i+length]
        return ""