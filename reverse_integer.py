class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 0:
            x_str = str(x)
            result =  int(x_str[::-1])
        if x < 0:
            x_str = str(x * (-1))
            result =  int('-'+(x_str[::-1]))

        #handling integer overflow
        max_int = 2**31 - 1

        if abs(result) > max_int:
            return 0
        else:
            return result


if __name__ == '__main__':

    x = -92
    instance = Solution()
    solution = instance.reverse(x)
    print(solution)
    print(type(solution))
