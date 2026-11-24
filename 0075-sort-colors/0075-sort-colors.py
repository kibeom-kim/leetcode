class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1
        
        idx = 0
        for color in range(3):
            freq = count_dict.get(color, 0)
            nums[idx: idx+freq] = [color] * freq
            idx += freq
            