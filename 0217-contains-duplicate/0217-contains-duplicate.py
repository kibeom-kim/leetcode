class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # d = dict()
        # for num in nums:
        #     if num in d:
        #         return True
            
        #     d[num] = True
        
        # return False
        
        return len(nums) != len({*nums})