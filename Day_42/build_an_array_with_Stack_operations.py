class Solution(object):
    def buildArray(self, target, n):
        """
        :type s: str
        :type indices: List
        :rtype: str
        """
        final = []
        for i in range(n):
            if i in target:
                final.append('Push')
            else:
                final.append('Push')
                final.append('Pop')
        return final    


if __name__ == '__main__':

    target = [1,3]
    n = 3

    instance = Solution()
    solution = instance.restoreString(target, n)

    print(solution)
