class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_value_idx_dict = defaultdict(list)
        for i, num in enumerate(nums):
            num_value_idx_dict[num].append(i)

        for i, num in enumerate(nums):
            sub_target = target - num
            sub_target_idx_list = num_value_idx_dict.get(sub_target, [])

            for idx in sub_target_idx_list:
                if i == idx:
                    continue
                
                return [i, idx]
        
        return []