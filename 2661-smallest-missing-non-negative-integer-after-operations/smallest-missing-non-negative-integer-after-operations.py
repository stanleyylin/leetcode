class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mods = [0]*(value)
        for num in nums:
            mods[num%value] += 1
        print(mods)
        
        mex = float('inf')
        for mod in range(value):
            candidate = mod + value * mods[mod]
            mex = min(mex, candidate)
        return mex
