class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        max_size = len(matrix)
        l = 0 
        r = max_size-1  
        t = 0 
        b = max_size-1 
        

        while(l < r): 
            for i in range(r-l):
                tl = matrix[t][l+i]
                tr = matrix[t+i][r]
                bl = matrix[b-i][l] 
                br = matrix[b][r-i]
                
                matrix[t+i][r] = tl 
                matrix[b][r-i] = tr 
                matrix[b-i][l] = br 
                matrix[t][l+i] = bl 

            t += 1 
            b -= 1 
            r -= 1 
            l += 1 
