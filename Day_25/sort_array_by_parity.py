class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lst = []
        for num in A:
            if num == 0:
                lst.insert(0, num)
            elif num%2 ==0:
                lst.insert(0, num)
            else:
                lst.insert(1,num)
        return lst

if __name__ == '__main__':

    points = [[3,2],[-2,2]]
    instance = Solution()
    solution = instance.minTimeToVisitAllPoints(points)

    print(solution)
