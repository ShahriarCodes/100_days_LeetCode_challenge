class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        low = 0
        high = len(S)
        A = []
        for s in S:
            if s == 'I':
                A.append(low)
                low += 1
            elif s == 'D':
                A.append(high)
                high -= 1
        return A + [low]


if __name__ == '__main__':

    S = "IDID"
    instance = Solution()
    solution = instance.diStringMatch(S)

    print(solution)
