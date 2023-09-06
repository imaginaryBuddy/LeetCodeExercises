class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        ro_0 = 1 
        for ro in range(len(matrix)):
            for co in range(len(matrix[0])):
                if matrix[ro][co] == 0 : 
                    if ro == 0: 
                        ro_0 = 0 # row 0 must all be 0 
                    else: 
                        matrix[ro][0] = 0 
                    matrix[0][co] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 

        if matrix[0][0] == 0: #turn the first col to 0, but ignore the first cell 
            for i in range(1, len(matrix)):
                matrix[i][0] = 0 

        if ro_0 == 0: #turn the whole row0 to 0
            for i in range(len(matrix[0])):
                matrix[0][i] = 0 

