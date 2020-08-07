class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        len_points = len(points)
        time  = 0
        for i in range(1, len_points):
            dx = abs(points[i][0] - points[i-1][0])
            dy = abs(points[i][1] - points[i-1][1])

            if dx > dy:
                time += dx
            else:
                time += dy




if __name__ == '__main__':

    points = [[1,1],[3,4],[-1,0]]
    instance = Solution()
    solution = instance.minTimeToVisitAllPoints(points)

    print(solution)
