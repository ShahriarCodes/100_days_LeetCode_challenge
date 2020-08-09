class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if (N <= 1):
            return N

        return self.fib(N - 1) + self.fib(N - 2)


if __name__ == '__main__':

    points = [[3,2],[-2,2]]
    instance = Solution()
    solution = instance.fib(points)

    print(solution)
