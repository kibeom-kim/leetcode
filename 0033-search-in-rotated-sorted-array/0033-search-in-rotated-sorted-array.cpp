class Solution {
public:
    int search(vector<int>& nums, int target) {
        int size = nums.size();
                             
        if(size == 0) return -1;
        if(nums[0] <= nums[size - 1]) return binarySearch(nums, 0, size-1, target);
       
        int pivot = findPivot(nums, 0, size-1);  
        if(nums[pivot] == target) return pivot;
        if(nums[0] <= target) return binarySearch(nums, 0, pivot-1, target);
        return binarySearch(nums, pivot+1, size-1, target);
    }
   
    int findPivot(vector<int> nums, int start, int end){
        while(start <= end){
            int mid = start + (end - start) / 2;
            
            if(nums[mid] > nums[mid+1]) return mid+1;
            
            if(nums[start] > nums[mid]) end = mid-1;
            else start = mid+1;
        }
        return -1;
    }
    
    int binarySearch(vector<int>nums, int start, int end, int target){
        while(start <= end){
            int mid = start + (end-start) / 2;        
            if(nums[mid] == target) return mid;
            else if(nums[mid] > target) end = mid - 1;
            else if(nums[mid] < target) start = mid + 1;
        }
        return -1;
    }
};