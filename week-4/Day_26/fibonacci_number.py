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

    N = 8
    instance = Solution()
    solution = instance.fib(N)

    print(solution)
