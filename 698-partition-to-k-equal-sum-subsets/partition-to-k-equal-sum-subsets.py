class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse = True) # biggest to smallest

        if nums[0] > target:
            return False
        
        buckets = [target] * k

        def backtrack(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if buckets[j] >= nums[i]:
                    buckets[j] -= nums[i]
                    if backtrack(i+1):
                        return True
                    # doesn't work
                    buckets[j] += nums[i]
                
                if buckets[j] == target:
                    break
            return False
        
        return backtrack(0)

