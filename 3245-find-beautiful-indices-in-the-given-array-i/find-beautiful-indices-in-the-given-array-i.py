class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        A = []
        start = 0
        while True:
            i = s.find(a, start)
            if i == -1:
                break
            A.append(i)
            start = i + 1

        B = [] 
        start = 0
        while True:
            i = s.find(b, start)
            if i == -1:
                break
            B.append(i)
            start = i + 1
        
        out = []
        for i in A:
            for j in B:
                if abs(i-j) <= k:
                    out.append(i)
                    break
        return out

