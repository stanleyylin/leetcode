class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(pattern, text):
            lps = [0] * len(pattern)
            j = 0
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                lps[i] = j
            out = []
            j = 0
            for i in range(len(text)):
                while j > 0 and text[i] != pattern[j]:
                    j = lps[j-1]
                if text[i] == pattern[j]:
                    j += 1
                if j == len(pattern):
                    out.append(i - j + 1)
                    j = lps[j - 1]
            return out
        A = kmp(a, s)
        B = kmp(b, s)
        
        out = []
        j = 0
        for i in A:
            while j < len(B) and B[j] < i - k: # direction is important
                j += 1
            if j < len(B) and abs(B[j]-i) <= k:
                out.append(i)

        return out

