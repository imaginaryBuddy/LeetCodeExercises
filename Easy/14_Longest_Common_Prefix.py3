class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:      
        strs.sort() 
        if (strs[0] == "" or len(strs)==1 or strs[0] == strs[len(strs)-1]):
            return strs[0]
        i = 0
        front = strs[0][0:i]
        back = strs[len(strs)-1][0:i] 
        last = len(strs)-1
        
        while(front == back):
            i+=1
            front = strs[0][0:i]
            back = strs[last][0:i]

        return front[0:i-1]
