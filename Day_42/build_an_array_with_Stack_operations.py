class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type indices: int
        :rtype: List[str]
        """
        final = []
        array = []
        for i in range(1, n+1):
            if array == target:
                break

            elif i in target:
                final.append('Push')
                array.append(i)

            elif i not in target:
                final.append('Push')
                final.append('Pop')
        return final


if __name__ == '__main__':

    target = [2,3,4]
    n = 4

    instance = Solution()
    solution = instance.buildArray(target, n)

    print(solution)
