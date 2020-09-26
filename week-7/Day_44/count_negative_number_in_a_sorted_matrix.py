class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        acc = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                
                    if grid[i][j] < 1:
                        acc += 1
        
        return acc

if __name__ == '__main__':
    grid =[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

    instance = Solution()
    solution = instance.countNegatives(grid)

    print(solution)

