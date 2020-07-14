class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 0:
            x_str = str(x)
            return int(x_str[::-1])
        else:
            x_str = str(x * (-1))
            return int('-'+(x_str[::-1]))



if __name__ == '__main__':

    x = -92
    instance = Solution()
    solution = instance.reverse(x)
    print(solution)
    print(type(solution))
