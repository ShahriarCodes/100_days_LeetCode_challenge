class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        nums = []
        for num in range(left, right+1):
            remainder = 0
            new_num = num
            j = 0
            for i in range(len(str(num))):
                remainder = new_num % 10
                if remainder != 0 and num % remainder == 0:
                    new_num = new_num // 10
                    j += 1

                else:
                    j= 0
                    break
            if j !=0:
                nums += [num]
        return nums


if __name__ == '__main__':

    left = 1
    right = 22
    instance = Solution()
    solution = instance.selfDividingNumbers(left, right)

    print(solution)


num = 22
remainder = 0
new_num = num
j = 0
for i in range(len(str(num))):
    remainder = new_num % 10
    if num % remainder == 0:
        new_num = new_num // 10
        j += 1

    else:
        j= 0
        break
