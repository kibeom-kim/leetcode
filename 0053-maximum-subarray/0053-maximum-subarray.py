class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        total = 0
        res = nums[0]
        
        for num in nums:
            if total < 0:
                total = 0
            
            total += num
            res = max(res, total)

        return res