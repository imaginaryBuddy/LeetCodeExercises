class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        s = len(nums)
        multL = [1]*s
        multR = [1]*s
        multL[0] = nums[0] 
        multR[-1] = nums[-1]
        for i in range(1,s-1):
            multL[i] = multL[i-1] * nums[i]
        for i in range(s-2, 0,-1):
            multR[i] = multR[i+1] * nums[i]
        for i in range(0,s):
            if (i == 0): 
                nums[i] = 1 * multR[i+1] 
            elif (i == s-1):
                nums[i] = 1* multL[i-1]
            else:
                nums[i] = multL[i-1] * multR[i+1]
        return nums
