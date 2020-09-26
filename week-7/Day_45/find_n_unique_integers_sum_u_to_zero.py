class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lst = []
        #for even n
        if n%2 == 0:
            for i in range(1,int(n/2 + 1)):
                lst.append(i)
                lst.append(-i)
        elif n%2 != 0:
            for i in range(1, int(n/2 + 1)):
                lst.append(i)
                lst.append(-i)
            lst.append(0)
        return lst



if __name__ == '__main__':
    n = 7
    instance = Solution()
    solution = instance.sumZero(n)

    print(solution)
