class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        output = 0
        for start, end in zip(startTime, endTime):
            if queryTime >= start and queryTime <= end:
                output += 1

        return output



if __name__ == '__main__':
    startTime = [9,8,7,6,5,4,3,2,1]
    endTime = [10,10,10,10,10,10,10,10,10]
    queryTime = 5

    instance = Solution()
    solution = instance.busyStudent(startTime, endTime, queryTime)

    print(solution)
