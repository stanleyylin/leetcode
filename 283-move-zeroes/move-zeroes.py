class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0 and i + 1 < len(nums):
                j = i + 1
                while j < len(nums) - 1 and nums[j] == 0:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
            
        