class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        bitwise = 0
        for i in range(n):
            bitwise = bitwise ^ (start + 2*i)

        return bitwise



if __name__ == '__main__':

    n = 10
    start = 5
    instance = Solution()
    solution = instance.xorOperation(n, start)
    print(solution)
