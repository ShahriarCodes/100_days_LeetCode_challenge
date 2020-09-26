class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        len_points = len(points)
        time  = 0
        dx , dy = 0 , 0
        for i in range(1, len_points):
            dx = abs(points[i][0] - points[i-1][0])
            dy = abs(points[i][1] - points[i-1][1])

            if dx > dy:
                time += dx
            else:
                time += dy

        return time


if __name__ == '__main__':

    points = [[3,2],[-2,2]]
    instance = Solution()
    solution = instance.minTimeToVisitAllPoints(points)

    print(solution)
