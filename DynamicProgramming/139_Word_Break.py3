class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            w = s[i:]
            for word in wordDict:
                if word in w: 
                    if w[0:len(word)] != word:
                        # if the word is not the start 
                        continue 
                    elif len(word) == len(w):
                        dp[i] = True  
                    elif w[0: len(word)] == word: 
                        # the word is the start, take the len diff 
                        dp[i] = dp[i+len(word)] or dp[i]
                        if dp[i] == True: 
                            break 

        print(dp)
        return dp[0] 
