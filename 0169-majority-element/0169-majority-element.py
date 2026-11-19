class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # 1
        # res = majority = 0

        # d = defaultdict(int)
        # for num in nums:
        #     d[num] += 1

        #     if d[num] > majority:
        #         res = num
        #         majority = d[num]
        
        # return res
    
        # 2
        # return sorted(nums)[len(nums) // 2]

        # 3
        
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            
            if candidate == num:
                count += 1
            else:
                count -= 1
        
        return candidate
