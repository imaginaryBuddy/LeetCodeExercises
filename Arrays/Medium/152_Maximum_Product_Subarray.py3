class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
          using the dp approach below exceeds time limit. so I followed Neetcode's method, that's O(n) 
        '''
        # dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        # maxProd = nums[0]

        # for s in range(0, len(nums)):
        #     for e in range(0, len(nums)):
        #         if (e < s):
        #             continue
        #         elif (e == s):
        #             dp[e][s] = nums[e] 
        #             maxProd = max(maxProd, nums[e])
        #         else: 
        #             dp[s][e] = dp[s][e-1] * nums[e] 
        #             maxProd = max(dp[s][e], maxProd)

        # return maxProd
  
  
        '''
        Neetcode's method
        '''
        res = max(nums)
        curMin, curMax = 1,1 
        flag = 0 
        for n in nums: 
            if n == 0:
                curMin, curMax = 1, 1 
                flag = 1 
            tmp = curMax * n 
            curMax = max(tmp, curMin*n, n)
            curMin = min(tmp, curMin*n, n)
            res = max(res, curMax)

        if flag: 
            return max(res, 0)
        else:
            return res

        
