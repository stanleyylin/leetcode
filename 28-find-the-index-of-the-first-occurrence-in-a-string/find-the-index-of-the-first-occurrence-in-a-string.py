class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        # 1) Build LPS[i] = length of longest proper prefix of needle[:i+1] that is also a suffix
        # If waitI matched up to here and fail, how much of the prefix do I halready have matched
        lps = [0] * len(needle)
        j = 0 # length of prev longest prefix

        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]
            if needle[i] == needle[j]:
                j += 1
                lps[i] = j
        
        # 2) Do KMP search
        # i = index in haystack (points to the next char to read)
        # j = index in needle (number of chars matched so far)
        i = j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

        for i in range(n):
            if haystack[i:i + m] == needle:
                return i
        
        return -1