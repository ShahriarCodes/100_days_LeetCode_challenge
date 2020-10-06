class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = row 
        N = row
        
        for i in range(row):
            for j in range(i, col):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        print(matrix)
        
        for i in range(row):
            for j in range(int(col/2)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][N-1-j]
                matrix[i][N-1-j] = temp
        print(matrix)
