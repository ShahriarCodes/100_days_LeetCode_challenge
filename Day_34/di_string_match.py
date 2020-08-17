class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if S[0] == 'I':
            A = [0]
        elif S[0] == 'D':
            A = [len(S)]

        for i, s in enumerate(S):
            if s == 'I':
                A.append(A[i]+1)
            if s == 'D':
                A.append(A[i]-1)
        return A





if __name__ == '__main__':

    S = "IDID"
    instance = Solution()
    solution = instance.diStringMatch(S)

    print(solution)
