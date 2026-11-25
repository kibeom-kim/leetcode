class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        def binary_search(l, start, end, t):
            while start <= end:
                mid = start + (end - start) // 2

                if l[mid] == t:
                    return mid
                
                elif l[mid] < t:
                    start = mid + 1
                else:
                    end = mid - 1
            
            return -1

        def find_pivot(l, start, end):
            while start <= end:
                mid = start + (end - start) // 2
            
                if l[mid] > l[mid + 1]:
                     return mid + 1
            
                if(l[start] > l[mid]):
                    end = mid - 1
                else:
                    start = mid + 1
        
            return -1
        
        size = len(nums)
        # if(size == 0):
        #     return -1

        if nums[0] <= nums[size - 1]:
            return binary_search(nums, 0, size - 1, target)
        
        pivot = find_pivot(nums, 0, size - 1)
        if nums[pivot] == target:
            return pivot
        
        if nums[0] <= target:
            return binary_search(nums, 0, pivot - 1, target)
        
        return binary_search(nums, pivot + 1, size - 1, target)
    
        
            