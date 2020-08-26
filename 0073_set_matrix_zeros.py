'''
Convert each line to a binary number
For example:
2 3 4 5 0 1 2 will be converted to 1 1 1 1 0 1 1
if the coverted number is not equal to 2^(n) - 1, then that row is going be set to all zero
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        numm = (1 << m) - 1
        numn = (1 << n) - 1
        strm = bin(numm)[2:]
        strn = bin(numn)[2:]
        
        resrow = []
        for i in range(m):
            temp = ''.join(['1' if j != 0 else '0' for j in matrix[i]])
            if temp != strn:
                resrow.append(i)
        
        rescol = []
        for i in range(n):
            temp = ''.join(['1' if matrix[idd][i] != 0 else '0' for idd in range(m)])
            if temp != strm:
                rescol.append(i)
        
        #print(resrow)
        #print(rescol)
        
        for i in resrow:
            matrix[i] = [0] * n
        
        for i in rescol:
            for j in range(m):
                matrix[j][i] = 0
