class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        
        i_placeholder = set()
        j_placeholder = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    i_placeholder.add(i)
                    j_placeholder.add(j)


        for i in i_placeholder:
            matrix[i] = [0] * col
        
        for i in range(row):
            for j in j_placeholder:
                matrix[i][j] = 0
        print(matrix)
        print(i_placeholder, j_placeholder)


# space optimized
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        col_0 = True
        
        for i in  range(row):
            if matrix[i][0] == 0 : col_0 = False
            for j in range(1,col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in reversed(range(row)):
            for j in reversed(range(1,col)):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
            if col_0 == False: matrix[i][0] = 0
        
        print(matrix)

