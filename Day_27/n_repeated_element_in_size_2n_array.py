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

    A = [1,2,2,3,5,6]
    instance = Solution()
    solution = instance.repeatedNTimes(A)

    print(solution)
