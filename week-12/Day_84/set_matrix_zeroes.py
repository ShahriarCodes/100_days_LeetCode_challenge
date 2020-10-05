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
