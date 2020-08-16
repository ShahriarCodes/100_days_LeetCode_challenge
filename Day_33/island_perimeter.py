class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len_row = len(A)
        len_col = len(A[0])
        perimeter = 0
        peri_value = [4,3,2,1,0]
        for row in range(len_row):
            for col in range(len_col):
                if A[row][col] == 1:
                    # inner values
                    if row > 0 and col > 0 and row < len_row-1 and col < len_col-1:
                        # print('row: ', row, ' col: ', col)
                        perimeter += peri_value[A[row-1][col] + A[row+1][col] + A[row][col-1] +  A[row][col+1]]
                        # print (perimeter)

                    # top bounding values
                    if row == 0:
                        perimeter += peri_value[0 + A[row+1][col] + A[row][col-1] +  A[row][col+1]]
                        print('row: ', row, ' col: ', col)
                        print(perimeter)
                    # bottom bounding values
                    if row == len_row-1:
                        perimeter += peri_value[A[row-1][col] + 0 + A[row][col-1] +  A[row][col+1]]

                    # left bounding values
                    if col == 0 and row > 0 and row < len_row-1 :
                        perimeter += peri_value[A[row-1][col] + A[row+1][col] + 0 +  A[row][col+1]]

                    # right bounding values
                    if col == len_row-1 and row > 0 and row < len_row-1 :
                        perimeter += peri_value[A[row-1][col] + A[row+1][col] + A[row][col-1] +  0]

        return perimeter

if __name__ == '__main__':

    A = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
    instance = Solution()
    solution = instance.islandPerimeter(A)

    print(solution)
