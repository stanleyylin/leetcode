class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix = 0
        seen = defaultdict(int)
        seen[0] = 1
        for x in nums:
            prefix += x
            count += seen[prefix-k]
            seen[prefix] += 1
        return count

        # n = len(nums)
        # count = 0
        # for start in range(n):
        #     currSum = 0
        #     for end in range(start, n):
        #         currSum += nums[end]
        #         if currSum == k:
        #             count += 1
        # return count
        
