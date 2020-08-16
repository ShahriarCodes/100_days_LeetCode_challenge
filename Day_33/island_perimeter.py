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

# working solution
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        row, col = len(grid), len(grid[0])
        hashMap = dict()


        for i in range(row):
            for j in range(col):

                if grid[i][j] == 1:

                    hashMap[(i, j)] = 4

                    if i == j == 0:
                        continue

                    if (i, j-1) in hashMap:
                        hashMap[(i, j)] -= 2

                    if (i-1, j) in hashMap:
                        hashMap[(i, j)] -= 2

        return sum(hashMap.values())

# another solution
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

		#array of number of edges for each grid. You can also keep a rolling sum here.
        num_of_edges = []

		#iterating over list of lists
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                edges = 0

				#if the grid value is 1
                if grid[i][j] == 1:
                    edges=4

					#we check neighboring grids to see if values are one. I have used try except for ease but you can add an additional if condition to overcome exceptions
                    try:
                        if grid[i+1][j] ==1:
                            edges-=1
                    except:
                        pass

                    try:
                        if grid[i][j+1] ==1:
                            edges-=1
                    except:
                        pass

					#we check if j-1>=0 and i-1>=0 to check for the edges
                    try:
                        if j-1>=0 and grid[i][j-1] ==1:
                            edges-=1
                    except:
                        pass

                    try:
                        if i-1>=0 and grid[i-1][j] ==1:
                            edges-=1
                    except:
                        pass

                num_of_edges.append(edges)

	   #return the sum
	   return(sum(num_of_edges))


if __name__ == '__main__':

    A = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
    instance = Solution()
    solution = instance.islandPerimeter(A)

    print(solution)
