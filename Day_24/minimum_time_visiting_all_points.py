class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        len_points = len(points)
        # j = 0
        for i in range(1, len_points):
            for j in range(2):
                if points[i][j] > points[i-1][j]




if __name__ == '__main__':

    points = [[1,1],[3,4],[-1,0]]
    instance = Solution()
    solution = instance.minTimeToVisitAllPoints(points)

    print(solution)
