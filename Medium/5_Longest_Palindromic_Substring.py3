class Solution:
    def longestPalindrome(self, s: str) -> str:
      # for edge case 
        if s == s[::-1]:
            return s
        l = len(s)
        maxLength = 1 
        res = s[0]
        dp = [[0 for i in range(l)] for j in range(l)]
        
        # fill the 2d array in a diagonal way 
        for colRowDiff in range(l):
            for ro in range(l-colRowDiff):
                col = ro + colRowDiff
                if col == ro :
                    dp[ro][col] = 1 
                    continue
                if (s[ro] == s[col] and dp[ro+1][col-1] == 1) or (s[ro] == s[col] and col-ro+1 == 2):
                        dp[ro][col] = 1
                        if maxLength < col-ro+1:
                            res = s[ro:col+1]
                            maxLength = col-ro+1
                    

        return res
       
