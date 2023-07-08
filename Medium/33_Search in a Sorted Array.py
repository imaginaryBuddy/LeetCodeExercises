class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)-1 
        l = 0 
        while l <= r: 
            mid = l+(r-l)//2
            if nums[mid] == target: 
                return mid 
            
           # mid in left sorted portion 
            if nums[l] <= nums[mid]:
                # conditions to search the right portion
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1 

                # conditions to search the left portion
                else:
                    r = mid - 1 
            
            # mid in right portion
            else: 
                # conditiosn to search the left portion
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1

                # conditions to search the left portion
                else:
                    l = mid + 1
        return -1
