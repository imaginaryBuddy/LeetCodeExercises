class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i+1):
                if nums[j] < nums[i] : 
                    count[i] = max(count[i], count[j]+1)
                
        
        return max(count)
