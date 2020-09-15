class Solution:
    def generateTheString(self, n: int) -> str:
        if n %2 == 0:
            st = 'a'*(n-1)
            st += 'b'
        else:
            st = 'a'*n
        return st
