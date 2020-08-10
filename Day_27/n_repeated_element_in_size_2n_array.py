class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dict = {}

        for num in A:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
                return num


if __name__ == '__main__':

    N = 8
    instance = Solution()
    solution = instance.fib(N)

    print(solution)
