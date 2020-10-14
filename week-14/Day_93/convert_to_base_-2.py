class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0 :
            return '0'
        acc = '' 
        while N != 0:
            if abs(N%2) == 1:
                acc += '1'
                N = (N - 1)/-2
            else:
                acc += '0'
                N = N/-2
        return acc[::-1]
