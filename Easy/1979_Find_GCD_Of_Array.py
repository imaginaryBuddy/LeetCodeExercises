class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxEle = max(nums)
        minEle = min(nums)
        gcd = 1
        for i in range(1,minEle+1):
            if maxEle%i ==0 and minEle%i==0:
                gcd = i 

        return gcd
