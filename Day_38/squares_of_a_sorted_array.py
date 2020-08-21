class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        square = []
        for a in A:
            square.append(a*a)
        return sorted(square)


if __name__ == '__main__':

    nums =  [-4,-1,0,3,10]
    instance = Solution()
    solution = instance.sortedSquares(nums)

    print(solution)
