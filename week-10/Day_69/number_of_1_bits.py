class Solution:
    def hammingWeight(self, n: int) -> int:
        # count = 0
        # for s in bin(n):
        #     if s == '1':
        #         count += 1
        # return count
        return bin(n).count('1')
